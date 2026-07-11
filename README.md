# jinja2-josa-filter 모노레포

Jinja2 호환 템플릿 환경에서 사용할 수 있는 한국어 조사 필터 패키지 레포지토리입니다. [tjosa](https://github.com/hsl0/tjosa) 라이브러리를 기반으로 만들었습니다.

## 패키지

- PyPI 패키지: `jinja2-josa-filter`
- Ansible Galaxy 컬렉션: `hsl0.josa`

## 구조

- `src/jinja2_josa_filter`: PyPI에 배포하는 Python 패키지입니다.
- `src/ansible_collections/hsl0/josa`: Ansible Galaxy에 배포하는 컬렉션입니다.

Ansible 컬렉션은 `src/ansible_collections` 아래에 둡니다. 이렇게 하면 `src`가 `PYTHONPATH`에 있을 때 실제 Ansible 컬렉션 import 경로와 같은 구조로 개발할 수 있습니다.

## 관계

`jinja2-josa-filter`는 `tjosa`를 기반으로 하며, Jinja2를 사용하는 모든 환경에서 쓸 수 있는 중립적인 Python 필터 패키지입니다.

`hsl0.josa` Ansible 컬렉션은 얇은 어댑터입니다. Ansible Galaxy에서 설치할 수 있으며, 설치하면 별도의 등록 과정 없이 바로 사용 가능합니다.

vendored dependency는 소스 저장소의 원본으로 관리하지 않습니다. Ansible Galaxy 컬렉션을 빌드할 때 `python-vendorize vendorize.toml`이 루트의 `vendorize.toml` 설정을 읽어 `plugins/module_utils/vendor` 아래에 필요한 패키지를 넣습니다.

## 개발 환경

```sh
pip install .[dev]
```

## 빌드

PyPI 패키지 (버전은 `pypi/vX.Y.Z` 태그에서 [hatch-vcs](https://github.com/ofek/hatch-vcs)가 자동으로 계산합니다):

```sh
python -m build
```

Ansible Galaxy 컬렉션 (`galaxy.yml`의 `version`은 `0.0.0` placeholder이므로 빌드 전 원하는 버전으로 직접 바꿔줍니다):

```sh
sed -i "s/^version:.*/version: <원하는 버전>/" src/ansible_collections/hsl0/josa/galaxy.yml
python-vendorize vendorize.toml
ansible-galaxy collection build src/ansible_collections/hsl0/josa --output-path dist
```

컬렉션의 filter plugin은 빌드 시 `plugins/module_utils/vendor` 아래에 주입된 패키지를 다음 경로로 import합니다.

```python
from ansible_collections.hsl0.josa.plugins.module_utils.vendor.jinja2_josa_filter import (
    JINJA_FILTERS,
)
```

## 확인

```sh
pytest
```

## 릴리스

`jinja2-josa-filter` 패키지와 `hsl0.josa` 컬렉션은 서로 독립적으로, git 태그를 기준으로 배포됩니다. 별도의 버전 bump 커밋은 없습니다 — 버전은 태그에서 유도됩니다.

| 태그 형식 | 대상 | 트리거되는 워크플로 |
|---|---|---|
| `pypi/vX.Y.Z` | PyPI 패키지 `jinja2-josa-filter` | `.github/workflows/release-pypi.yml` |
| `ansible-collection/vX.Y.Z` | Ansible Galaxy 컬렉션 `hsl0.josa` | `.github/workflows/release-collection.yml` |

- `jinja2-josa-filter` 버전은 `pypi/vX.Y.Z` 태그로부터 [hatch-vcs](https://github.com/ofek/hatch-vcs)가 자동으로 계산합니다. `pyproject.toml`에는 정적 버전 문자열이 없습니다.
- `hsl0.josa` 컬렉션 버전은 `galaxy.yml`에 `0.0.0` placeholder로만 존재하며, 릴리스 빌드 시 `ansible-collection/vX.Y.Z` 태그 값이 주입됩니다.
- 패키지 소스가 바뀌어 컬렉션도 같이 갱신해야 한다면 같은 커밋에 두 태그를 함께 push합니다. 컬렉션 어댑터 코드만 바뀐 경우에는 `ansible-collection/v*` 태그만 push하면 됩니다. 컬렉션은 로컬 소스를 벤더링하므로 PyPI 배포 완료를 기다릴 필요가 없습니다.
- 레거시 role은 배포하지 않습니다. Galaxy의 legacy role import는 GitHub 레포 루트에 role이 있어야 하는데, 모노레포 서브디렉토리에 있는 role은 직접 배포가 불가능하기 때문입니다. 컬렉션 필터는 기본적으로 FQCN(`hsl0.josa.<필터명>`)으로 사용하며, 짧은 이름이 필요하면 컬렉션 README의 "짧은 이름으로 사용하기" 절을 참고하세요.

## 라이선스

MIT
