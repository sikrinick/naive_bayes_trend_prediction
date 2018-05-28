from .calculable import Calculable


class EMA(Calculable):

    def __calc__(self):
        super().__calc__()
        self._check_specific_field_("adj_close_str")

        data = self._data(self._column_names.adj_close_str)
        result = []
        start = self._mem - 1
        data_size = len(data)

        weight = 2 / (self._mem + 1)

        for i in range(start, data_size):
            prev = i - start - 1
            if prev < 0:
                ema = sum(data[i - start: i + 1]) / self._mem
            else:
                ema = weight * data[i] + (1 - weight) * result[prev]
            result.append(ema)
        return result
