from pandas import DataFrame
from indicators import ColumnNames

class Weighter:

    def fit(self,
            data: DataFrame,
            column_names: ColumnNames,
            strategies: DataFrame) -> list:
        pass

    def predict(self,
                data: DataFrame,
                column_names: ColumnNames) -> DataFrame:
        pass

