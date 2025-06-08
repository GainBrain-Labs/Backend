from enum import IntEnum

class stock_group_type(IntEnum):
    NIFTY50 = 1
    NIFTY100 = 2
    NIFTY200 = 3
    NIFTY500 = 4
    CUSTOM = 5

class compare_type(IntEnum):
    INTRA = 1
    INTER = 2