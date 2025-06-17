from enum import Enum

class DefaultStockGroupType(Enum):
    NIFTY50 = "NIFTY50"
    NIFTY100 = "NIFTY100"
    NIFTY200 = "NIFTY200"
    NIFTY500 = "NIFTY500"
    
class BacktestProcessingStatus(Enum):
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"

class CompareType(Enum):
    INTRA = "INTRA"
    INTER = "INTER"
