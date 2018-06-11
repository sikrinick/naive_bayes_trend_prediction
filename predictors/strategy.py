from indicators import *
from tests import run_tests
import matplotlib.pyplot as plt
from numpy import std


class Strategy:

    def __init__(self,
                 main_set: DataFrame,
                 column_names: ColumnNames,
                 starting_money: int,
                 order_size: int,
                 transaction_percent: float,
                 training_set_size: int = 80,
                 default_memories: int = 10,
                 risk_free_rate: float = 3.5):
        self.main_set = main_set
        self.column_names = column_names
        self.starting_money = starting_money
        self.order_size = order_size
        self.transaction_percent = transaction_percent
        self.training_set_size = training_set_size
        self.default_memories = default_memories
        self.risk_free_rate = risk_free_rate

    l = [x for x in range(10) if x % 2 != 0]

    def run(self):
        run_tests()

        set_size = len(self.main_set)
        training_proc_end = int(self.training_set_size * set_size / 100)
        testing_proc_start = training_proc_end
        training_set = self.main_set.iloc[:training_proc_end]
        testing_set = self.main_set.iloc[testing_proc_start:]

        # For testing purposes
        # sma = SMA(training_set, memory, column_names).result
        # ema = EMA(training_set, memory, column_names).result
        # mom = Momentum(training_set, memory, column_names).result

        stck = STCK(training_set, self.default_memories, self.column_names)
        stcd = STCD(stck.result.to_frame("STCK"), self.default_memories)
        lwr = LWR(training_set, self.default_memories, self.column_names)
        # ado = ADO(training_set, memory, column_names).result # Bad performance
        cci = CCI(training_set, self.default_memories, self.column_names)
        rsi = RSI(training_set, self.default_memories, self.column_names)
        # macd = MACD(training_set, memory, column_names).result # Bad performance

        prices = training_set[self.column_names.adj_close_str]
        inds = {stck: STCK, stcd: STCD, lwr: LWR, cci: CCI, rsi: RSI}

        best = 0
        best_ind = None

        print("Training")
        print("Indicator Result Sharpe")
        for indicator in inds.keys():
            changes = self.run_strat(prices, indicator)
            ind_name = indicator.__class__.__name__
            print("%s: %f, %f" %
                  (ind_name, sum(changes) + self.starting_money, self.sharpe(changes)))

            plt.title("%s strategy" % ind_name)
            plt.plot(indicator.strategy.values)
            plt.show()
            plt.title("%s changes" % ind_name)
            plt.plot(self.starting_money + changes.values)
            plt.show()
            result = sum(changes) + self.starting_money
            if result > best:
                best_ind = inds[indicator]
                best = result

        print("\n")

        print("Best: %s %f" % (best_ind.__name__, best))
        if best_ind == STCD:
            stck = STCK(testing_set, self.default_memories, self.column_names)
            test_result = STCD(stck.result.to_frame("STCK"), self.default_memories)
        else:
            test_result = best_ind(testing_set, self.default_memories, self.column_names)

        prices = testing_set[self.column_names.adj_close_str]
        changes = self.run_strat(prices, test_result)
        result = sum(changes) + self.starting_money

        print("\n")
        print("Testing result: %f" % result)
        print("Testing sharpe: %f" % self.sharpe(changes))
    def sharpe(self, changes):
        rets = (sum(changes) / len(changes) / self.starting_money) * 100 + 100
        return (rets - self.risk_free_rate) / std(changes) * 1000

    def run_strat(self, prices, indicator):
        money = self.starting_money
        changes = []
        transaction_costs = 0
        amounts = 0
        dates = []

        for idx in indicator.strategy.index:
            strat = indicator.strategy[idx]
            if strat != Calculable.HOLD:
                raw_money = self.order_size * prices[idx]
                if idx == indicator.strategy.index[-1]:
                    raw_money = amounts * prices[idx]
                    strat = Calculable.SELL
                transaction_cost = self.transaction_percent * raw_money / 100
                order_expense = raw_money * strat + transaction_cost
                if (strat == Calculable.BUY and money >= order_expense)\
                        or \
                        (strat == Calculable.SELL and amounts >= self.order_size):
                    transaction_costs += transaction_cost
                    amounts += strat * self.order_size
                    dates.append(idx)
                    changes.append(-order_expense)
                    money -= order_expense
        return Series(data=changes, index=dates)

