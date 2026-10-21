from abc import ABC, abstractmethod
from typing import Final

class Editor(ABC):
    _pdf_files: Final[str[]]

    def __init__(self, pdf_files: str[]) -> None:
        self._pdf_files = pdf_files

    @abstractmethod
    def ask(self) -> bool:
        pass

    @abstractmethod
    def run(self) -> None:
        pass