from indicators import SMA, EMA, CalculableError


def sma_test():
    data = [11, 12, 13, 14, 15, 16, 17]
    sma = SMA(data, 5)
    assert sma.result == [13, 14, 15]


def ema_test():
    data = [5.3, 6.7, 7.9, 7.1, 5.2]
    ema = EMA(data, 4)
    assert ema.result == [6.75, 6.13]


def ma_mem_error_test():
    data = [11, 12]
    try:
        SMA(data, 3).result
    except CalculableError as e:
        assert True


if __name__ == '__main__':
    sma_test()
    ema_test()
    ma_mem_error_test()
    print("Finished, at least SMA and EMA are correct")
