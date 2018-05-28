from .calculable import Calculable

class SMA(Calculable):

    def __calc__(self):
        super().__calc__()
        self._check_specific_field_("adj_close_str")

        data = self._data[self._column_names.adj_close_str]
        result = []
        data_size = len(data)
        start = self._mem - 1

        for i in range(start, data_size):
            ma = sum(data[i - start: i + 1]) / self._mem
            result.append(ma)

        return result

