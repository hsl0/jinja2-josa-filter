"""plugins/filter/*.yml 문서와 템플릿을 합쳐 필터 플러그인 .py를 만듭니다."""

import ast
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FILTER_DIR = ROOT / "src/ansible_collections/hsl0/josa/plugins/filter"
SOURCE = ROOT / "src/jinja2_josa_filter/__init__.py"
# name과 aliases는 모듈 로드 때 한 번 딕셔너리로 만들어 두고 filters()는 그대로 반환
TEMPLATE = r'''# 자동 생성된 파일입니다. 직접 수정하지 마세요. (tools/generate_filter_plugins.py)
DOCUMENTATION = r"""
@DOCUMENTATION@"""

EXAMPLES = r"""
@EXAMPLES@"""

RETURN = r"""
@RETURN@"""

from ansible_collections.hsl0.josa.plugins.plugin_utils.vendor.jinja2_josa_filter import (
    @FUNCTION@,
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


def load_function_map():
    """src/jinja2_josa_filter의 JINJA_FILTERS에서 필터 이름 -> 함수 이름을 읽습니다."""
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and node.targets[0].id == "JINJA_FILTERS":
            return {k.value: v.id for k, v in zip(node.value.keys, node.value.values)}
    raise SystemExit(f"{SOURCE}: JINJA_FILTERS를 찾지 못했습니다")


def function_for(path, names, function_map):
    unknown = [n for n in names if n not in function_map]
    if unknown:
        raise SystemExit(f"{path.name}: JINJA_FILTERS에 없는 이름 {unknown}")
    functions = {function_map[n] for n in names}
    if len(functions) != 1:
        raise SystemExit(f"{path.name}: 이름들이 서로 다른 함수를 가리킵니다 {functions}")
    return functions.pop()


def render(data, names, function):
    filters = "".join(
        f"    {json.dumps(n, ensure_ascii=False)}: {function},\n" for n in names
    )
    text = TEMPLATE.replace("@FILTERS@", filters).replace("@FUNCTION@", function)
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
    function_map = load_function_map()
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
        names = filter_names(yml, data)
        function = function_for(yml, names, function_map)
        out.write_text(
            render(data, names, function), encoding="utf-8", newline="\n"
        )
        generated.add(out.name)

    remove_stale(generated)
    print(f"generated {len(generated)} filter plugins")


if __name__ == "__main__":
    sys.exit(main())
