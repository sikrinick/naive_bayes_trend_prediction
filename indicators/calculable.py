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
    def result(self) -> list:
        if self._result is None:
            self._result = self.__calc__()
        return self._result

    @abstractmethod
    def __calc__(self):
        data_size = len(self._data)
        if data_size < self._mem:
            raise CalculableError("Data size is lower than memory!")

    def _check_specific_field_(self, field: str):
        if self._column_names is None or getattr(self._column_names, field) is None:
            raise RuntimeError("No field %s specified!" % field)
