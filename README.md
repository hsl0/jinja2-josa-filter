# jinja2-josa-filter 모노레포

Jinja2 호환 템플릿 환경에서 사용할 수 있는 한국어 조사 필터 패키지 레포지토리입니다. [tjosa](https://github.com/hsl0/tjosa) 라이브러리를 기반으로 만들었습니다.

## 패키지

- PyPI 패키지: `jinja2-josa-filter`
- Ansible Galaxy 컬렉션: `hsl0.josa`

## 구조

- `src/jinja2_josa_filter`: PyPI에 배포하는 Python 패키지입니다.
- `src/ansible_collections/hsl0/josa`: Ansible Galaxy에 배포하는 컬렉션입니다.
- `scripts/build-pypi.sh`: PyPI 배포용 빌드 스크립트입니다.
- `scripts/build-ansible-galaxy.sh`: Ansible Galaxy 컬렉션 빌드 스크립트입니다.

Ansible 컬렉션은 `src/ansible_collections` 아래에 둡니다. 이렇게 하면 `src`가 `PYTHONPATH`에 있을 때 실제 Ansible 컬렉션 import 경로와 같은 구조로 개발할 수 있습니다.

## 관계

`jinja2-josa-filter`는 `tjosa`를 기반으로 하며, Jinja2를 사용하는 모든 환경에서 쓸 수 있는 중립적인 Python 필터 패키지입니다.

`hsl0.josa` Ansible 컬렉션은 얇은 어댑터입니다. Ansible Galaxy에서 설치할 수 있으며, 설치하면 별도의 등록 과정 없이 바로 사용 가능합니다.

vendored dependency는 소스 저장소의 원본으로 관리하지 않습니다. Ansible Galaxy 컬렉션을 빌드할 때 `python-vendorize`가 `pyproject.toml`의 `[tool.vendorize]` 설정을 읽어 `plugins/module_utils/vendor` 아래에 필요한 패키지를 넣습니다.

## 개발 환경

```sh
pip install .[dev]
```

## 빌드

PyPI 패키지:

```sh
./scripts/build-pypi.sh
```

Ansible Galaxy 컬렉션:

```sh
./scripts/build-ansible-galaxy.sh
```

Ansible Galaxy 빌드는 `python-vendorize` 실행 후 `ansible-galaxy collection build .`를 실행합니다.

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

## 라이선스

MIT
