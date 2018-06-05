from .calculable import Calculable
from pandas import DataFrame


class STCK(Calculable):

    def __calc__(self) -> DataFrame:

        low_data = self._data[self._column_names.low_str]
        high_data = self._data[self._column_names.high_str]
        close_data = self._data[self._column_names.close_str]

        dates = []
        values = []

        start = self._mem - 1
        for i in range(start, len(close_data)):
            min_price = min(low_data[i - start: i + 1])
            max_price = max(high_data[i - start: i + 1])
            stck = (close_data[i] - min_price) / (max_price - min_price)

            dates.append(self._data.index.values[i])
            values.append(stck)

        df = DataFrame(data={"STCK": values}, index=dates)
        df.index.name = "Date"
        return df

