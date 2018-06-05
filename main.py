from indicators import ColumnNames, SMA, EMA, Momentum
from indicators import STCK, STCD, LWR, ADO, CCI, RSI, MACD
import pandas as pd


if __name__ == '__main__':

    main_set = pd.read_csv("data/MA.csv", index_col=0)
    main_set = main_set

    column_names = ColumnNames(
        open_str="Open",
        close_str="Close",
        low_str="Low",
        high_str="High",
        adj_close_str="Adj Close",
        volume_str="Volume")

    memory = 10

    results = {}

    for classname in (SMA, EMA, Momentum, STCK,
                      LWR, ADO, CCI, RSI, MACD):
        results[classname.__name__] = \
            classname(main_set, memory, column_names).result

    results[STCD.__name__] = STCD(results[STCK.__name__], memory).result
