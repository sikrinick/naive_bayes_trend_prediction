from abc import ABC, abstractmethod
from pandas import DataFrame
from .calculable_error import CalculableError
from .columnnames import ColumnNames


class Calculable(ABC):

    def __init__(self,
                 data: DataFrame,
                 mem: int = None,
                 column_names: ColumnNames= None):
        self._data = data
        self._mem = mem
        self._column_names = column_names
        self._result = None

    @property
    def result(self) -> DataFrame:
        if self._result is None:
            self._result = self.__calc__()
        return self._result

    @abstractmethod
    def __calc__(self):
        pass
