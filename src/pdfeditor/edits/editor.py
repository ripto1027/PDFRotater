from abc import ABC, abstractmethod

class Editor(ABC):
    def __init__(self, pdf_files: list[str]) -> None:
        self._pdf_files = pdf_files

    @abstractmethod
    def run(self) -> None:
        pass