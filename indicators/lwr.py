from .calculable import Calculable
from pandas import DataFrame


class LWR(Calculable):

    def __calc__(self) -> DataFrame:

        low_data = self._data[self._column_names.low_str]
        high_data = self._data[self._column_names.high_str]
        close_data = self._data[self._column_names.close_str]

        dates = []
        values = []

        start = self._mem - 1
        for i in range(start, len(close_data)):
            min_price = min(low_data[i - start: i + 1])
            max_price = max(high_data[i - start: i + 1])
            lwr = (max_price - close_data[i]) / (max_price - min_price) * -100

            dates.append(self._data.index.values[i])
            values.append(lwr)

        df = DataFrame(data={"LWR": values}, index=dates)
        df.index.name = "Date"
        return df
    #
    # Williams
    # used
    # a
    # 10
    # trading
    # day
    # period and considered
    # values
    # below - 80 as oversold and above - 20 as overbought.But
    # they
    # were
    # not to
    # be
    # traded
    # directly, instead
    # his
    # rule
    # to
    # buy
    # an
    # oversold
    # was
    #
    # % R
    # reaches - 100 %.
    # Five
    # trading
    # days
    # pass
    # since - 100 % was
    # last
    # reached
    # % R
    # fall
    # below - 95 % or -85 %.
    # or conversely
    # to
    # sell
    # an
    # overbought
    # condition
    #
    # % R
    # reaches
    # 0 %.
    # Five
    # trading
    # days
    # pass
    # since
    # 0 % was
    # last
    # reached
    # % R
    # rise
    # above - 5 % or -15 %.
    # The
    # timeframe
    # can
    # be
    # changed
    # for either more sensitive or smoother results.The more sensitive you make it, though, the more false signals you will get.
    #
    def __strategy__(self):
        pass

