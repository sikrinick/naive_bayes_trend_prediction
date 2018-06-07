from .calculable import Calculable
from pandas import DataFrame


class SMA(Calculable):

    def __calc__(self) -> DataFrame:

        data = self._data[self._column_names.adj_close_str]
        data_size = len(data)

        dates = []
        values = []

        start = self._mem - 1
        for i in range(start, data_size):
            ma = sum(data[i - start: i + 1]) / self._mem
            dates.append(self._data.index.values[i])
            values.append(ma)
        df = DataFrame(data={"SMA": values}, index=dates)
        df.index.name = "Date"
        return df

    def __strategy__(self):
        # No strat
        pass
