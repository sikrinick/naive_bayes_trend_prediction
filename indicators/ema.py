from .calculable import Calculable
from pandas import Series


class EMA(Calculable):

    def __calc__(self) -> Series:
        data = self._data[self._column_names.adj_close_str].values
        start = self._mem - 1
        data_size = len(data)
        dates = []
        values = []
        weight = 2 / (self._mem + 1)

        for i in range(start, data_size):
            prev = i - start - 1
            if prev < 0:
                ema = sum(data[i - start: i + 1]) / self._mem
            else:
                ema = weight * data[i] + (1 - weight) * values[prev]
            dates.append(self._data.index.values[i])
            values.append(ema)

        df = Series(data=values, index=dates)
        df.index.name = "Date"
        return df

    def __strategy__(self):
        # TODO ADD STRATEGY
        pass

