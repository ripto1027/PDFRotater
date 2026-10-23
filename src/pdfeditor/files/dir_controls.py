import os

from pathlib import Path
from typing import Final

__BASE_DIR: Final[Path] = Path(os.environ["USERPROFILE"]) / "PdfEditor"
INPUT_DIR: Final[Path] = __BASE_DIR / "input"
OUTPUT_DIR: Final[Path] = __BASE_DIR / "output"

def exists_input_dir() -> bool:
    return INPUT_DIR.is_dir()

def exists_output_dir() -> bool:
    return OUTPUT_DIR.is_dir()

def create_input_dir() -> None:
    INPUT_DIR.mkdir(parents=True, exist_ok=True)

def create_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def open_input_dir() -> None:
    os.startfile(INPUT_DIR)

def open_output_dir() -> None:
    os.startfile(OUTPUT_DIR)
    