from pathlib import Path
def read_lines(path : str):
    file_path=Path(path)

    if not file_path :
        raise FileNotFoundError("File doesn't found at path : {path}")
    
    with file_path.open("r",encoding="utf-8") as f:
        for line in f:
            yield line