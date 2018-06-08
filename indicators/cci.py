from .calculable import Calculable
from pandas import Series


class CCI(Calculable):

    def __calc__(self) -> Series:
        high_data = self._data[self._column_names.high_str]
        low_data = self._data[self._column_names.low_str]
        close_data = self._data[self._column_names.close_str]

        data_size = len(close_data)

        Ms = [(high_data[i] + low_data[i] + close_data[i]) / 3 for i in range(data_size)]

        SMs = []

        start = self._mem - 1

        for i in range(start, data_size):
            sm = sum(Ms[i - start: i + 1]) / self._mem
            SMs.append(sm)

        Ds = []

        start = self._mem - 1
        for i in range(start, data_size):
            coefs = [abs(Ms[x] - SMs[i - start]) for x in range(i - start, i + 1)]
            d = sum(coefs) / self._mem
            Ds.append(d)

        dates = []
        values = []

        for i in range(start, data_size):
            coef = (Ms[i] - SMs[i - start]) / (0.015 * Ds[i - start])
            dates.append(self._data.index.values[i])
            values.append(coef)

        df = Series(data=values, index=dates)
        df.index.name = "Date"
        return df

    def __strategy__(self):
        dates = []
        strat = []

        for date in self.result.index:
            value = self.result.loc[date]

            pos = Calculable.HOLD
            if value < -100:
                pos = Calculable.BUY
            elif value > 100:
                pos = Calculable.SELL

            dates.append(date)
            strat.append(pos)

        df = Series(data=strat, index=dates)
        df.index.name = "Date"
        return df
