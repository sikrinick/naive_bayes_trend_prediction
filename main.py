import pandas as pd
from utils import ColumnNames
from predictors import Strategy

if __name__ == '__main__':

    main_set = pd.read_csv("data/MA.csv", index_col=0)
    column_names = ColumnNames(
        open_str="Open",
        close_str="Close",
        low_str="Low",
        high_str="High",
        adj_close_str="Adj Close",
        volume_str="Volume")
    money = 100000
    amount = 100
    training_percent = 80
    memory = 10
    transaction_cost_percent = 0.05

    strat = Strategy(main_set,
                     column_names,
                     money,
                     amount,
                     transaction_cost_percent,
                     training_percent,
                     memory)

    strat.run()









