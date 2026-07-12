# jinja2-josa-filter

Jinja2 호환 템플릿 환경에서 사용할 수 있는 한국어 조사 필터 패키지 레포지토리입니다. [tjosa](https://github.com/hsl0/tjosa-py) 라이브러리를 기반으로 만들었습니다.

## 패키지 목록

- **[jinja2-josa-filter](src/jinja2_josa_filter/README.md)** (PyPI): Jinja2를 사용하는 모든 환경에서 쓸 수 있는 중립적인 Python 패키지입니다.
- **[hsl0.josa](src/ansible_collections/hsl0/josa/README.md)** (Ansible 컬렉션): 위 패키지를 Ansible 컬렉션으로 다시 배포한 어댑터입니다. 공개 Ansible Galaxy 인덱스에는 게시하지 않고, GitHub Release에서만 배포합니다. 설치 후 별도 등록 없이 바로 사용할 수 있습니다.

## 사용법

두 패키지 모두 같은 조사 필터 세트를 제공하며, 등록 방식만 다릅니다. 등록 방법은 각 패키지 README를 참고하세요.

```jinja2
{{ food | 는 }} 맛있다.
>> 사과는 맛있다.
>> 파인애플은 맛있다.

{{ building | 은 }} 크다.
>> 집은 크다.
>> 학교는 크다.

{{ animal | 이 }} 잔다.
>> 고양이가 잔다.
>> 표범이 잔다.

{{ drink | 를 }} 마신다.
>> 물을 마신다.
>> 콜라를 마신다.

{{ tools[0] | 과 }} {{ tools[1] }}
>> 책과 깃펜
>> 컴퓨터와 마우스

말은 {{ horse | 로 }}, 사람은 {{ human | 으로 }}
>> 말은 제주로, 사람은 서울로

{{ friend | 야 }}, 안녕~
>> 철수야, 안녕~
>> 지민아, 안녕~

{{ friend | 이는 }} 내 친구
>> 철수는 내 친구
>> 지민이는 내 친구
```

제공하는 필터:

- `은는`, `은`, `는`
- `이가`, `가`
- `을를`, `을`, `를`
- `과와`, `과`, `와`
- `으로`, `로`
- `아야`, `아`, `야`
- `이`, `이랑`, `랑`, `이며`, `며`, `이다`, `다`

## 개발 가이드

### 개발 환경 설정

```sh
pip install '.[dev]'
```

### 의존성 번들링

`hsl0.josa` 컬렉션은 `jinja2_josa_filter`와 `tjosa`를 vendoring해서 배포합니다. vendored 코드는 저장소에 원본으로 관리하지 않으며, 실행 전에 반드시 vendorize를 거쳐야 합니다.

```sh
python-vendorize
```

### 린트

`jinja2-josa-filter` 패키지는 flake8과 pylint를 사용합니다.

```sh
flake8 src/jinja2_josa_filter/**.py
pylint src/jinja2_josa_filter
```

`hsl0.josa` 컬렉션은 `ansible-test`의 `sanity`를 사용합니다. sanity는 flake8과 pylint에서 수행하는 검사를 포함하므로 flake8과 pylint 검사를 별도로 수행할 필요가 없습니다.

```sh
cd src/ansible_collections/hsl0/josa
ansible-test sanity
```

### 테스트

`jinja2-josa-filter` 패키지는 `pytest`를 사용합니다.

```sh
pytest
```

`hsl0.josa` 컬렉션은 `ansible-test`의 통합 테스트를 사용합니다.

```sh
cd src/ansible_collections/hsl0/josa
ansible-test integration
```


## 라이선스

MIT
