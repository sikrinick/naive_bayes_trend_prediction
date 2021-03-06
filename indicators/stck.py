from .calculable import Calculable
from pandas import Series


class STCK(Calculable):

    def __calc__(self) -> Series:

        low_data = self._data[self._column_names.low_str]
        high_data = self._data[self._column_names.high_str]
        close_data = self._data[self._column_names.close_str]

        dates = []
        values = []

        start = self._mem - 1
        for i in range(start, len(close_data)):
            min_price = min(low_data[i - start: i + 1])
            max_price = max(high_data[i - start: i + 1])
            stck = ((close_data[i] - min_price) / (max_price - min_price)) * 100

            dates.append(self._data.index.values[i])
            values.append(stck)

        df = Series(data=values, index=dates)
        df.index.name = "Date"
        return df

    def __strategy__(self) -> Series:
        dates = []
        strat = []

        for date in self.result.index:
            value = self.result.loc[date]

            pos = Calculable.HOLD
            if value < 20:
                pos = Calculable.BUY
            elif value > 80:
                pos = Calculable.SELL

            dates.append(date)
            strat.append(pos)

        df = Series(data=strat, index=dates)
        df.index.name = "Date"
        return df

