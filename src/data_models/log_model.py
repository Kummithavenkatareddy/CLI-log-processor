from dataclasses import dataclass
from typing import Literal

LogLevel = Literal["INFO", "ERROR", "DEBUG", "WARNING", "CRITICAL"]

@dataclass(frozen=True)
class LogEntry:
    timestamp: str
    level: LogLevel
    module: str
    message: str
