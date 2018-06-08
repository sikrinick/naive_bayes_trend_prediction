from .calculable import Calculable
from pandas import Series


class ADO(Calculable):

    def __calc__(self) -> Series:

        open_data = self._data[self._column_names.open_str]
        low_data = self._data[self._column_names.low_str]
        high_data = self._data[self._column_names.high_str]
        close_data = self._data[self._column_names.close_str]

        dates = []
        values = []

        for i in range(len(close_data)):

            open = open_data[i]
            high = high_data[i]
            low = low_data[i]
            close = close_data[i]

            ado = (((high - open) + (close - low)) / (2 * (high - low))) * 100

            dates.append(self._data.index.values[i])
            values.append(ado)

        df = Series(data=values, index=dates)
        df.index.name = "Date"
        return df
