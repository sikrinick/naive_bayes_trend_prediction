from .calculable import Calculable
from pandas import DataFrame


class EMA(Calculable):

    def __calc__(self) -> DataFrame:
        data = self._data[self._column_names.adj_close_str]
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

        df = DataFrame(data={"EMA": values}, index=dates)
        df.index.name = "Date"
        return df

