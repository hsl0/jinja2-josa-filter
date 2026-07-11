from ansible_collections.hsl0.josa.plugins.module_utils.vendor.jinja2_josa_filter import (
    JINJA_FILTERS,
)


class FilterModule:
    @staticmethod
    def filters():
        return JINJA_FILTERS
