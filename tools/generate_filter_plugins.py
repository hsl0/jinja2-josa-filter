"""plugins/filter/*.yml 문서와 템플릿을 합쳐 필터 플러그인 .py를 만듭니다."""

import json
import re
import sys
from pathlib import Path

import yaml

FILTER_DIR = (
    Path(__file__).resolve().parents[1]
    / "src/ansible_collections/hsl0/josa/plugins/filter"
)
# name과 aliases는 모듈 로드 때 한 번 딕셔너리로 만들어 두고 filters()는 그대로 반환
TEMPLATE = r'''# 자동 생성된 파일입니다. 직접 수정하지 마세요. (tools/generate_filter_plugins.py)
DOCUMENTATION = r"""
@DOCUMENTATION@"""

EXAMPLES = r"""
@EXAMPLES@"""

RETURN = r"""
@RETURN@"""

from ansible_collections.hsl0.josa.plugins.plugin_utils.vendor.jinja2_josa_filter import (
    JINJA_FILTERS,
)

_FILTERS = {
@FILTERS@}


class FilterModule:
    @staticmethod
    def filters():
        return _FILTERS
'''
HEADER = TEMPLATE.splitlines(keepends=True)[0]
SECTIONS = ("DOCUMENTATION", "EXAMPLES", "RETURN")
GALAXY_NAME = re.compile(r"^(?!.*__)[a-z_][0-9a-z_]*$")


def load_docs(path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    missing = [key for key in SECTIONS if key not in data]
    if missing:
        raise SystemExit(f"{path.name}: {', '.join(missing)} 섹션이 없습니다")
    return data


def filter_names(path, data):
    doc = data["DOCUMENTATION"]
    if doc["name"] != path.stem:
        raise SystemExit(
            f"{path.name}: name({doc['name']})이 파일명({path.stem})과 다릅니다"
        )
    return (doc["name"], *doc.get("aliases", ()))


def literal(name, value):
    if not isinstance(value, str):
        value = yaml.safe_dump(value, allow_unicode=True, sort_keys=False)
    if '"""' in value:
        raise SystemExit(f'{name}: """를 포함하는 문서는 지원하지 않습니다')
    return value


def render(data, names):
    filters = "".join(
        f"    {json.dumps(n, ensure_ascii=False)}: "
        f"JINJA_FILTERS[{json.dumps(n, ensure_ascii=False)}],\n"
        for n in names
    )
    text = TEMPLATE.replace("@FILTERS@", filters)
    for key in SECTIONS:
        text = text.replace(f"@{key}@", literal(key, data[key]))
    return text


def remove_stale(keep):
    for path in FILTER_DIR.glob("*.py"):
        if path.name in keep or not path.read_text(encoding="utf-8").startswith(HEADER):
            continue
        path.unlink()
        print(f"removed stale {path.name}")


def main():
    owners = {}
    docs = {}
    for yml in sorted(FILTER_DIR.glob("*.yml")):
        docs[yml] = load_docs(yml)
        for name in filter_names(yml, docs[yml]):
            if name in owners:
                raise SystemExit(
                    f"필터 이름 {name}이 {owners[name]}와 {yml.name}에 중복됩니다"
                )
            owners[name] = yml.name

    generated = set()
    for yml, data in docs.items():
        out = yml.with_suffix(".py")
        if not GALAXY_NAME.match(out.stem):
            raise SystemExit(f"{out.name}: Galaxy가 받는 파일명이 아닙니다")
        out.write_text(
            render(data, filter_names(yml, data)), encoding="utf-8", newline="\n"
        )
        generated.add(out.name)

    remove_stale(generated)
    print(f"generated {len(generated)} filter plugins")


if __name__ == "__main__":
    sys.exit(main())
