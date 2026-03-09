# Log Level Counter

Simple Python utility that reads a plaintext log file, parses each line, and counts entries by log level (INFO, ERROR, DEBUG, WARNING, CRITICAL).

## Requirements

- Python 3.9+
- (Optional) install packages from `requirements.txt` if you use the included virtual environment or tools.

## Usage

Run the CLI with a path to a log file:

```bash
python -m src.main sample.log
```

Example output (a dictionary of counts):

```
{'INFO': 5, 'DEBUG': 2, 'WARNING': 2, 'ERROR': 2}
```

## Files

- `src/main.py` — entry point and orchestration.
- `src/Infrastructure/file_reader.py` — yields lines from the given file.
- `src/data_models/log_model.py` — `LogEntry` dataclass and `parse_line()`.
- `src/Infrastructure/processing_logic.py` — aggregates counts by level.

## Notes

- If you run into a `FileNotFoundError`, ensure the path is correct. Example: `sample.log` is included at the repository root.
