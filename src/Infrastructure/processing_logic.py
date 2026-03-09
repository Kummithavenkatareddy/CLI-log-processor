from collections import Counter
from typing import Iterable

from ..data_models.log_model import LogEntry, LogLevel

def count_levels(entries: Iterable[LogEntry]) -> dict[LogLevel, int]:
    counter: Counter[str] = Counter()

    for entry in entries:
        counter[entry.level] += 1

    return dict(counter)