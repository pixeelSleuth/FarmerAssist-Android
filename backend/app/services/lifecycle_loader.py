import json

from pathlib import Path
from functools import lru_cache


BASE_DIR = Path(__file__).resolve().parent.parent

LIFECYCLE_PATH = (
    BASE_DIR
    / "knowledge_base"
    / "lifecycle"
    / "Maize_Crop_Lifecycle_Dharwad-2.json"
)


@lru_cache(maxsize=1)
def load_lifecycle():

    with open(
        LIFECYCLE_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)