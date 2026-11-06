from ansible_collections.hsl0.josa.plugins.plugin_utils.vendor.jinja2_josa_filter import (
    a_ya,
    e,
    e_da,
    e_ga,
    e_myeo,
    e_rang,
    eu_ro,
    eul_reul,
    eun_neun,
    gwa_wa,
    josa,
)

# 충돌할 수 있는 영어 이름은 내보내지 않는다. 영어 이름은 FQCN으로만 쓴다.
_FILTERS = {
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


class FilterModule:
    @staticmethod
    def filters():
        return _FILTERS
