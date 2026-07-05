#!/usr/bin/python

from tjosa import josa_only
from tjosa.mappings.josa import BuiltinJosa


def josa(cheon: str, josa: BuiltinJosa) -> str:
    return cheon + josa_only(cheon, josa)


def eun_neun(cheon: str) -> str:
    return josa(cheon, "는")


def e_ga(cheon: str) -> str:
    return josa(cheon, "가")


def eul_reul(cheon: str) -> str:
    return josa(cheon, "를")


def gwa_wa(cheon: str) -> str:
    return josa(cheon, "과")


def eu_ro(cheon: str) -> str:
    return josa(cheon, "으로")


def a_ya(cheon: str) -> str:
    return josa(cheon, "야")


def e(cheon: str) -> str:
    return josa(cheon, "이")


def e_rang(cheon: str) -> str:
    return e(cheon) + "랑"


def e_myeo(cheon: str) -> str:
    return e(cheon) + "며"


def e_da(cheon: str) -> str:
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


__all__ = [
    "JINJA_FILTERS",
    "josa",
    "eun_neun",
    "e_ga",
    "eul_reul",
    "gwa_wa",
    "eu_ro",
    "a_ya",
    "e",
    "e_rang",
    "e_myeo",
    "e_da",
]
