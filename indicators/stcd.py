from .calculable import Calculable, ColumnNames
from .sma import SMA
from pandas import DataFrame


class STCD(Calculable):

    def __calc__(self) -> DataFrame:
        column_names = ColumnNames(adj_close_str="STCK")
        stcd = SMA(self._data, mem=self._mem, column_names=column_names).result
        stcd.columns = ["STCD"]
        return stcd

    def __strategy__(self):
        dates = []
        strat = []

        for date in self.result.index:
            value = self.result.loc[date]["STCD"]

            pos = Calculable.HOLD
            if value < 20:
                pos = Calculable.BUY
            elif value > 80:
                pos = Calculable.SELL

            dates.append(date)
            strat.append(pos)

        df = DataFrame(data={"STCD": strat}, index=dates)
        df.index.name = "Date"
        return df
