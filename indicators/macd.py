from .calculable import Calculable
from .ema import EMA
from utils.columnnames import ColumnNames
from pandas import Series


class MACD(Calculable):

    def __calc__(self) -> Series:

        slow_ema = EMA(self._data, 26, self._column_names).result
        fast_ema = EMA(self._data, 12, self._column_names).result
        fast_ema = fast_ema.loc[slow_ema.index.values[0]:]

        return EMA(slow_ema - fast_ema, self._mem, column_names=ColumnNames(adj_close_str="EMA")).result

    def __strategy__(self):
        # TODO ADD STRATEGY
        pass

