from indicators import SMA, EMA, CalculableError, ColumnNames
from pandas import DataFrame


def sma_test(column_names):
    sma_dates = [0, 1, 2, 3, 4, 5, 6]
    sma_data = [11, 12, 13, 14, 15, 16, 17]
    sma_df = DataFrame(data={"Test": sma_data}, index=sma_dates)
    sma_df.index.name = "Date"
    sma = SMA(sma_df, 5, column_names)
    assert list(sma.result["SMA"].values) == [13, 14, 15]


def ema_test(column_names):
    ema_dates = [0, 1, 2, 3, 4]
    ema_data = [5.3, 6.7, 7.9, 7.1, 5.2]
    ema_df = DataFrame(data={"Test": ema_data}, index=ema_dates)
    ema_df.index.name = "Date"
    ema = EMA(ema_df, 4, column_names)
    assert list(ema.result["EMA"].values) == [6.75, 6.13]


def ma_mem_error_test(column_names):
    sma_dates = [1, 2]
    sma_data = [11, 12]
    sma_df = DataFrame(data={"Test": sma_data}, index=sma_dates)
    sma_df.index.name = "Date"
    try:
        SMA(sma_df, 3, column_names).result
    except CalculableError as e:
        assert True


def run_tests():
    column_names = ColumnNames(adj_close_str="Test")
    sma_test(column_names)
    ema_test(column_names)
    ma_mem_error_test(column_names)
    print("Finished, at least SMA and EMA are correct")


if __name__ == '__main__':
    run_tests()

