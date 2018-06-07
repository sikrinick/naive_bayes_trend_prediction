from indicators import *
import pandas as pd
import numpy as np
from tests import run_tests
import matplotlib.pyplot as plt


if __name__ == '__main__':

    run_tests()

    main_set = pd.read_csv("data/MA.csv", index_col=0)

    set_size = len(main_set)

    training_proc_end = int(0.6 * set_size)
    testing_proc_start = training_proc_end
    training_set = main_set.iloc[:training_proc_end]
    testing_set = main_set.iloc[testing_proc_start:]

    column_names = ColumnNames(
        open_str="Open",
        close_str="Close",
        low_str="Low",
        high_str="High",
        adj_close_str="Adj Close",
        volume_str="Volume")

    memory = 10

    # For testing purposes
    # sma = SMA(training_set, memory, column_names).result
    # ema = EMA(training_set, memory, column_names).result
    # mom = Momentum(training_set, memory, column_names).result

    stck = STCK(training_set, memory, column_names)
    stcd = STCD(stck.result, memory)
    lwr = LWR(training_set, memory, column_names)
    # ado = ADO(training_set, memory, column_names).result
    cci = CCI(training_set, memory, column_names)
    rsi = RSI(training_set, memory, column_names)
    # macd = MACD(training_set, memory, column_names).result

    df = stck.strategy\
        .join(stcd.strategy)\
        .join(lwr.strategy)\
        .join(cci.strategy)\
        .join(rsi.strategy)

    df.dropna(inplace=True)


    for idx, row in df.iterrows():
        #calculate profits

        pass







