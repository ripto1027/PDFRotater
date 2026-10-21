import os
from rotatepdf.files.dir_controls import DirControls as controls
from typing import Final

class PdfEditList:
    __pdf_list: list[str]

    def __init__(self) -> None:
        if not controls.exists_input_dir():
            controls.missing_input_dir()

        unfiltered_input_files = os.listdir(controls.input_dir)
        input_files = [f for f in unfiltered_input_files if PdfEditList.__is_pdf_file]
        if len(input_files) == 0:
            controls.missing_pdf_file()

        self.__pdf_list = input_files

    @staticmethod
    def __is_pdf_file(file_name: str) -> bool:
        return file_name.lower().endswith(".pdf")

    @property
    def get_pdf_list(self) -> list[str]:
        return self.__pdf_list