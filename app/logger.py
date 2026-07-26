import logging
from pathlib import Path

# logs klasörü yoksa oluştur
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/clipforge.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("ClipForge")