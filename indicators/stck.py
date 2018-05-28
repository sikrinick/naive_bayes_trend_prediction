from .calculable import Calculable


class STCK(Calculable):

    def __calc__(self) -> list:
        super().__calc__()
        self._check_specific_field_("low_str")
        self._check_specific_field_("high_str")
        self._check_specific_field_("close_str")


