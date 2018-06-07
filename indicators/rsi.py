from .calculable import Calculable
from pandas import DataFrame
from .ema import EMA
from .columnnames import ColumnNames


class RSI(Calculable):

    def __calc__(self) -> DataFrame:
        close_data = self._data[self._column_names.close_str]
        Us = []
        Ds = []
        for i in range(1, len(close_data)):
            cur = close_data[i]
            prev = close_data[i - 1]
            Us.append(cur - prev if cur > prev else 0)
            Ds.append(prev - cur if prev > cur else 0)
        u_ema = EMA(DataFrame({"U": Us}), self._mem, column_names=ColumnNames(adj_close_str="U")).result
        d_ema = EMA(DataFrame({"D": Ds}), self._mem, column_names=ColumnNames(adj_close_str="D")).result


        dates = []
        values = []

        start = self._mem + 1 - 1
        for i in range(start, len(close_data)):
            date = self._data.index.values[i]

            rs = u_ema["EMA"].values[i-start] / d_ema["EMA"].values[i-start]
            rsi = 100 - (100 / (1 + rs))

            dates.append(date)
            values.append(rsi)

        df = DataFrame(data={"RSI": values}, index=dates)
        df.index.name = "Date"
        return df

    def __strategy__(self):
        dates = []
        strat = []

        for date in self.result.index:
            value = self.result.loc[date]["RSI"]

            pos = Calculable.HOLD
            if value < 20:
                pos = Calculable.BUY
            elif value > 80:
                pos = Calculable.SELL

            dates.append(date)
            strat.append(pos)

        df = DataFrame(data={"RSI": strat}, index=dates)
        df.index.name = "Date"
        return df