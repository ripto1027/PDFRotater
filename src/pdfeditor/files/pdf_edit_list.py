import os

from typing import Final

from pdfeditor.files.dir_controls import INPUT_DIR, exists_input_dir
from pdfeditor.files.dir_exceptions import missing_input_dir, missing_pdf_file

class PdfEditList:
    __pdf_list: Final[list[str]]

    def __init__(self) -> None:
        if not exists_input_dir():
            missing_input_dir()

        unfiltered_input_files = os.listdir(INPUT_DIR)
        input_files = [f for f in unfiltered_input_files if PdfEditList.__is_pdf_file(f)]
        if len(input_files) == 0:
            missing_pdf_file()

        self.__pdf_list = input_files

    @staticmethod
    def __is_pdf_file(file_name: str) -> bool:
        return file_name.lower().endswith(".pdf")

    @property
    def get_pdf_list(self) -> list[str]:
        return self.__pdf_list