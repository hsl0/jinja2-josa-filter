from __future__ import annotations

from jinja2_josa_filter import JINJA_FILTERS, e_ga, eun_neun, josa


def test_public_filters_apply_josa() -> None:
    assert eun_neun("사과") == "사과는"
    assert eun_neun("집") == "집은"
    assert e_ga("사과") == "사과가"
    assert e_ga("집") == "집이"


def test_jinja_filters_exports_filter_mapping() -> None:
    assert JINJA_FILTERS["은는"] is eun_neun
    assert JINJA_FILTERS["josa"] is josa
    assert JINJA_FILTERS["은는"]("집") == "집은"
