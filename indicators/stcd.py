from .calculable import Calculable, ColumnNames
from .sma import SMA
from pandas import DataFrame


class STCD(Calculable):

    def __calc__(self) -> DataFrame:
        column_names = ColumnNames(adj_close_str="STCK")
        stcd = SMA(self._data, mem=self._mem, column_names=column_names).result
        stcd.columns = ["STCD"]
        return stcd
