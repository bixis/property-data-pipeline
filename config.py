from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)


BASE_DIR = Path(__file__).resolve().parent

DATABASE_PATH = BASE_DIR / "properties.db"
LOG_DIR = BASE_DIR / "logs"
EXPORT_DIR = BASE_DIR / "exports"

LOG_DIR.mkdir(exist_ok=True)
EXPORT_DIR.mkdir(exist_ok=True)



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("property_pipeline")
