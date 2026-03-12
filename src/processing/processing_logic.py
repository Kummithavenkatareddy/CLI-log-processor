from collections import Counter
from typing import Iterable

from ..data_models.log_model import LogEntry, LogLevel

counter: Counter[str] = Counter()

def count_levels(entry: LogEntry) -> dict[LogLevel, int]:

    counter[entry.level] += 1

    return dict(counter)