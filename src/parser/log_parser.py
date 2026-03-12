from src.data_models.log_model import LogEntry, LogLevel

VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

def parse_line(line: str) -> LogEntry:
    parts = line.strip().split(" | ")

    if len(parts) != 4:
        raise ValueError("Malformed log line")

    timestamp, level, module, message = parts

    if level not in VALID_LEVELS:
        raise ValueError(f"Unknown log level: {level}")

    return LogEntry(
        timestamp=timestamp,
        level=level,  
        module=module,
        message=message,
    )