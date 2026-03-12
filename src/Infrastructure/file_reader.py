from pathlib import Path
from typing import Iterator


def read_lines(path: str) -> Iterator[str]:
    file_path = Path(path)

    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(f"File not found at path: {path}")

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            yield line