from enum import Enum, IntEnum

class StockGroupType(IntEnum):
    NIFTY50 = 1
    NIFTY100 = 2
    NIFTY200 = 3
    NIFTY500 = 4
    CUSTOM = 5

class CompareType(IntEnum):
    INTRA = 1
    INTER = 2
    
class BacktestProcessingStatus(Enum):
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"
