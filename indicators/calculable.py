from abc import ABC, abstractmethod
from pandas import DataFrame, Series
from utils.columnnames import ColumnNames


class Calculable(ABC):

    BUY = 1
    HOLD = 0
    SELL = -1

    def __init__(self,
                 data: DataFrame,
                 mem: int = None,
                 column_names: ColumnNames = None):
        self._data = data
        self._mem = mem
        self._column_names = column_names
        self._result = None
        self._strategy = None

    @property
    def result(self) -> Series:
        if self._result is None:
            self._result = self.__calc__()
        return self._result

    @property
    def strategy(self) -> Series:
        if self._strategy is None:
            self._strategy = self.__strategy__()
        return self._strategy

    @abstractmethod
    def __calc__(self):
        pass

    @abstractmethod
    def __strategy__(self):
        pass

    @abstractmethod
    def __trend__(self):
        pass