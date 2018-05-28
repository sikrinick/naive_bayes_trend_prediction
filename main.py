from indicators import ColumnNames, SMA, EMA, Momentum, STCK
import pandas as pd
import numpy as np


if __name__ == '__main__':

    main_set = pd.read_csv("data/MA.csv")
    main_set = main_set

    column_names = ColumnNames(open_str="Open", close_str="Close", low_str="Low", high_str="High",
                               adj_close_str="Adj Close", volume_str="Volume")

    sma = SMA(main_set, 10, column_names)
    ema = EMA(main_set, 10, column_names)
    momentum = Momentum(main_set, 10, column_names)
    st

    r = momentum.result