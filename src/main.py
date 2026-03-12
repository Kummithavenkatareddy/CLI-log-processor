import logging
import sys
from src.Infrastructure.file_reader import read_lines
from src.processing.processing_logic import count_levels
from src.parser.log_parser import parse_line
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

MAX_BAD_LINES= 10000
MAX_BAD_RATIO= 0.50

def main() :
    if len(sys.argv) != 2 :
        print("usage : python -m src.main <logfile>")
        return 1
    
    path = sys.argv[1]
    bad_lines=0
    total_lines=0
    entries=[]
    try: 
        for line in read_lines(path):
            total_lines+=1

            try:
                entry=parse_line(line)
                entries.append(entry)
            except ValueError:
                bad_lines+=1
                logger.warning("Malformed Lines")

                if bad_lines > MAX_BAD_LINES or bad_lines / total_lines > MAX_BAD_RATIO:
                    logger.error("corrupted dataset")
                    return 1
        counts = count_levels(entries)

        logger.info("processing_complete")
        print(counts)

        if bad_lines > 0:
            print(f"Malformed lines: {bad_lines}")

        return 0
    except FileNotFoundError:
        logger.error("file_not_found", extra={"path": path})
        return 1

if __name__ == "__main__":
    sys.exit(main())