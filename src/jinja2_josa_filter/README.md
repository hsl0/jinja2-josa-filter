# jinja2-josa-filter

Jinja2 호환 템플릿 환경에서 사용할 수 있는 한국어 조사 필터 패키지입니다. [tjosa](https://github.com/hsl0/tjosa-py) 라이브러리를 바탕으로 만들었습니다.

## 참고

이 패키지는 Jinja2에 직접 의존하지 않습니다. 일반 Python callable과 필터 매핑을 제공하며, 애플리케이션이나 프레임워크가 제공하는 Jinja2 호환 환경에 등록해서 사용합니다.

## 등록

이 패키지는 개별 필터 함수와 `JINJA_FILTERS` 매핑을 내보냅니다. 다음과 같이 런타임에 필터를 등록해 사용할 수 있습니다. 자세한 등록 방법은 사용하고자 하는 프레임워크의 도움말을 참고하세요.

```python
from jinja2_josa_filter import JINJA_FILTERS

app_or_framework_jinja_env.filters.update(JINJA_FILTERS)
```

개별 필터 함수도 직접 import할 수 있습니다.

```python
from jinja2_josa_filter import eun_neun, e_ga, eul_reul
```

## 사용

템플릿에서는 다음처럼 사용할 수 있습니다.

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

## 필터 종류

- `은는`, `은`, `는`
- `이가`, `가`
- `을를`, `을`, `를`
- `과와`, `과`, `와`
- `으로`, `로`
- `아야`, `아`, `야`
- `이`, `이랑`, `랑`, `이며`, `며`, `이다`, `다`

## 라이선스

MIT
