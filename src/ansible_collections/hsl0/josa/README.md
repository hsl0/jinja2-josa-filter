# hsl0.josa

Jinja2 용 한국어 조사 필터를 제공하는 Ansible 컬렉션입니다. [tjosa](https://github.com/hsl0/tjosa-py) 라이브러리를 바탕으로 만들어진 [jinja2-josa-filter](https://github.com/hsl0/jinja2-josa-filter/tree/main/src/jinja2_josa_filter) 패키지를 Ansible에 맞게 다듬었습니다.

## 요구 사항

필터 플러그인이 실행되는 Ansible 컨트롤러 노드가 **Python 3.12 이상** 버전에서 실행되어야 합니다.

## 설치

이 컬렉션은 `는`, `은`, `가`, `를` 같은 한글 필터 이름을 그대로 노출합니다. 공개 Ansible
Galaxy 인덱스는 필터 이름에 ASCII 영문·숫자·밑줄만 허용하기 때문에, 이 컬렉션은 Galaxy에
게시하지 않고 **GitHub Release**로 직접 배포합니다.

```sh
# 최신 버전 — 릴리스마다 URL이 바뀌지 않습니다
ansible-galaxy collection install --force \
  https://github.com/hsl0/jinja2-josa-filter/releases/download/ansible-collection/latest/hsl0-josa.tar.gz

# 마이너 버전 고정 (0.1.x 최신)
ansible-galaxy collection install --force \
  https://github.com/hsl0/jinja2-josa-filter/releases/download/ansible-collection/v0.1/hsl0-josa.tar.gz

# 정확한 버전 고정
ansible-galaxy collection install \
  https://github.com/hsl0/jinja2-josa-filter/releases/download/ansible-collection/v0.1.0/hsl0-josa.tar.gz
```

`latest`나 `v0.1`처럼 채널 URL로 설치하거나 업그레이드할 때는 `--force`를 붙여야 합니다.
URL 설치는 기본적으로 기존 설치본이 있으면 건너뛰기 때문입니다.

## 사용

Ansible에서 컬렉션 필터는 기본적으로 FQCN(Fully Qualified Collection Name)으로 참조합니다.

```jinja2
{{ food | hsl0.josa.는 }} 맛있다.
>> 사과는 맛있다.
>> 파인애플은 맛있다.

{{ building | hsl0.josa.은 }} 크다.
>> 집은 크다.
>> 학교는 크다.

{{ animal | hsl0.josa.가 }} 잔다.
>> 고양이가 잔다.
>> 표범이 잔다.

{{ drink | hsl0.josa.를 }} 마신다.
>> 물을 마신다.
>> 콜라를 마신다.

{{ tools[0] | hsl0.josa.과 }} {{ tools[1] }}
>> 책과 깃펜
>> 컴퓨터와 마우스

말은 {{ horse | hsl0.josa.로 }}, 사람은 {{ human | hsl0.josa.으로 }}
>> 말은 제주로, 사람은 서울로

{{ friend | hsl0.josa.야 }}, 안녕~
>> 철수야, 안녕~
>> 지민아, 안녕~

{{ friend | hsl0.josa.이 }}는 내 친구
>> 철수는 내 친구
>> 지민이는 내 친구
```

### 짧은 이름으로 사용하기 (FQCN 생략)

`는`, `은`과 같이 `hsl0.josa.` 접두어를 생략한 짧은 이름으로 필터를 쓰고 싶다면 플레이북과 같은 디렉터리에 `filter_plugins/josa.py`를 만들고 컬렉션의 `FilterModule`을 재노출하는 파일을 만드세요.

```python
from ansible_collections.hsl0.josa.plugins.filter.josa import FilterModule
```

Ansible은 플레이북 옆의 `filter_plugins/`를 자동으로 인식하므로, 별도 설정 없이 `{{ food | 는 }}`처럼 짧은 이름을 바로 쓸 수 있습니다.

## 필터

- `은는`, `은`, `는`
- `이가`, `가`
- `을를`, `을`, `를`
- `과와`, `과`, `와`
- `으로`, `로`
- `아야`, `아`, `야`
- `이`, `이랑`, `랑`, `이며`, `며`, `이다`, `다`

## 라이선스

MIT
