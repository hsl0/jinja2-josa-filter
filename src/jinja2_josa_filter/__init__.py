#!/usr/bin/python

"""Jinja2 호환 템플릿 환경에서 사용할 수 있는 한국어 조사 필터 모음입니다."""

from tjosa import josa_only as _josa_only
from tjosa.mappings.josa import BuiltinJosa as _BuiltinJosa


def josa(cheon: str, josa: _BuiltinJosa) -> str:
    """체언과 조사를 입력해서 체언에 맞는 조사를 반환합니다.

    Args:
        cheon: 조사를 붙일 체언
        josa: 선택할 조사 후보 중 하나

    Returns:
        체언에 알맞은 조사가 붙은 문자열

    Examples:
        >>> josa("사과", "는")
        '사과는'
        >>> josa("집", "는")
        '집은'
    """

    return cheon + _josa_only(cheon, josa)


def eun_neun(cheon: str) -> str:
    """체언 뒤에 보조사 '은/는'을 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        체언에 '은' 또는 '는'이 붙은 문자열

    Examples:
        >>> eun_neun("사과")
        '사과는'
        >>> eun_neun("집")
        '집은'
    """

    return josa(cheon, "는")


def e_ga(cheon: str) -> str:
    """체언 뒤에 주격 조사 '이/가'를 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        체언에 '이' 또는 '가'가 붙은 문자열

    Examples:
        >>> e_ga("학교")
        '학교가'
        >>> e_ga("고양이")
        '고양이가'
    """

    return josa(cheon, "가")


def eul_reul(cheon: str) -> str:
    """체언 뒤에 목적격 조사 '을/를'을 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        체언에 '을' 또는 '를'이 붙은 문자열

    Examples:
        >>> eul_reul("콜라")
        '콜라를'
        >>> eul_reul("물")
        '물을'
    """

    return josa(cheon, "를")


def gwa_wa(cheon: str) -> str:
    """체언 뒤에 접속 조사 '과/와'를 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        체언에 '과' 또는 '와'가 붙은 문자열

    Examples:
        >>> gwa_wa("책")
        '책과'
        >>> gwa_wa("마우스")
        '마우스와'
    """

    return josa(cheon, "과")


def eu_ro(cheon: str) -> str:
    """체언 뒤에 방향/수단 조사 '으로/로'를 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        체언에 '으로' 또는 '로'가 붙은 문자열

    Examples:
        >>> eu_ro("서울")
        '서울로'
        >>> eu_ro("집")
        '집으로'
    """

    return josa(cheon, "으로")


def a_ya(cheon: str) -> str:
    """체언 뒤에 호격 조사 '아/야'를 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        체언에 '아' 또는 '야'가 붙은 문자열

    Examples:
        >>> a_ya("철수")
        '철수야'
        >>> a_ya("지민")
        '지민아'
    """

    return josa(cheon, "야")


def e(cheon: str) -> str:
    """체언 뒤에 서술격 조사 어간 '이'를 필요할 때만 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        받침이 있는 체언에는 '이'가 붙은 문자열을, 받침이 없으면 체언을 그대로 반환합니다.

    Examples:
        >>> e("철수")
        '철수'
        >>> e("지민")
        '지민이'
    """

    return josa(cheon, "이")


def e_rang(cheon: str) -> str:
    """체언 뒤에 '이랑/랑'을 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        체언에 '이랑' 또는 '랑'이 붙은 문자열

    Examples:
        >>> e_rang("철수")
        '철수랑'
        >>> e_rang("지민")
        '지민이랑'
    """

    return e(cheon) + "랑"


def e_myeo(cheon: str) -> str:
    """체언 뒤에 '이며/며'를 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        체언에 '이며' 또는 '며'가 붙은 문자열

    Examples:
        >>> e_myeo("철수")
        '철수며'
        >>> e_myeo("지민")
        '지민이며'
    """

    return e(cheon) + "며"


def e_da(cheon: str) -> str:
    """체언 뒤에 '이다/다'를 붙입니다.

    Args:
        cheon: 조사를 붙일 체언

    Returns:
        체언에 '이다' 또는 '다'가 붙은 문자열

    Examples:
        >>> e_da("철수")
        '철수다'
        >>> e_da("지민")
        '지민이다'
    """

    return e(cheon) + "다"


JINJA_FILTERS = {
    "josa": josa,
    "은는": eun_neun,
    "은": eun_neun,
    "는": eun_neun,
    "이가": e_ga,
    "가": e_ga,
    "을를": eul_reul,
    "을": eul_reul,
    "를": eul_reul,
    "과와": gwa_wa,
    "과": gwa_wa,
    "와": gwa_wa,
    "으로": eu_ro,
    "로": eu_ro,
    "아야": a_ya,
    "아": a_ya,
    "야": a_ya,
    "이": e,
    "이랑": e_rang,
    "랑": e_rang,
    "이며": e_myeo,
    "며": e_myeo,
    "이다": e_da,
    "다": e_da,
}
