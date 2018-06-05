from .calculable import Calculable
from pandas import DataFrame


class Momentum(Calculable):

    def __calc__(self) -> DataFrame:
        data = self._data[self._column_names.adj_close_str]
        dates = []
        values = []
        data_size = len(data)
        start = self._mem - 1

        for i in range(start, data_size):
            mom = data[i] - data[i - start]
            dates.append(self._data.index.values[i])
            values.append(mom)
        df = DataFrame(data={"Momentum": values}, index=dates)
        df.index.name = "Date"
        return df

