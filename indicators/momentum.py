from .calculable import Calculable


class Momentum(Calculable):

    def __calc__(self):
        super().__calc__()
        if self._column_names is None:
            raise RuntimeError("No field specified!")

        data = self._data[self._column_names]
        result = []
        data_size = len(data)
        start = self._mem - 1

        for i in range(start, data_size):
            ma = data[i] - data[i - start]
            result.append(ma)

        return result

