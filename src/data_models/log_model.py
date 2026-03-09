from dataclasses import dataclass
from typing import Literal

LogLevel = Literal["INFO", "ERROR", "DEBUG", "WARNING", "CRITICAL"]

@dataclass(frozen=True)
class LogEntry:
    timestamp: str
    level: LogLevel
    module: str
    message: str

def parse_line(line : str) -> LogEntry:
    parts = line.strip().split(" | ")
    if len(parts) != 4:
        raise ValueError("Malformed Log Line")
    
    timestamp, level, module, message = parts

    if level not in {"INFO", "ERROR", "DEBUG", "WARNING", "CRITICAL"}:
        raise ValueError(f"unknown log level: {level}")
    
    return LogEntry( 
        timestamp=timestamp,
        level=level,
        module=module,
        message=message,
    )
