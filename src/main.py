import logging
import sys
from src.Infrastructure.file_reader import read_lines
from src.Infrastructure.processing_logic import count_levels
from src.data_models.log_model import parse_line
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

def main() :
    if len(sys.argv) != 2 :
        print("usage : python -m src.main <logfile>")
        return 1
    
    path = sys.argv[1]

    try: 
        lines = read_lines(path)
        entries=(parse_line(line) for line in lines)
        counts=count_levels(entries)
        logger.info("log_summary", extra={"counts": counts})
        print(counts)
    except FileNotFoundError:
        logger.error("file_not_found", extra={"path": path})
        return 1
    except ValueError as e:
        logger.error("parse_error", extra={"error": str(e)})
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())