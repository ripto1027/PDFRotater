import os

from pathlib import Path
import sys
from pypdf import PdfReader, PdfWriter

from pdfeditor.edits.editor import Editor
from pdfeditor.files.dir_controls import INPUT_DIR, OUTPUT_DIR, exists_output_dir, open_output_dir
from pdfeditor.files.dir_exceptions import missing_output_dir
from pdfeditor.utils import pause

class Rotater(Editor):
    __rotate_angle: int

    def __init__(self, pdf_files: list[str]) -> None:
        super().__init__(pdf_files)

    def __ask(self) -> None:
        print("inputフォルダにあるPDFを時計回りに回転させます。")

        tmp_angle: int = self.__get_rotate_angle()
        if tmp_angle == 0:
            print("回転角度が無効です。プログラムを終了します。")
            pause()
            print("")
            sys.exit()

        self.__rotate_angle = tmp_angle

    def __get_rotate_angle(self) -> int:
        tmp_angle: str = input("何度回転させますか？(90, 180, 270): ")
        print("")

        if tmp_angle not in ["90", "180", "270"]:
            print("回転させる角度は90, 180, 270のいずれかを指定してください。")
            input_continue: str = input("やり直しますか？(Y/N): ")
            print("")

            if input_continue.lower() == "y":
                return self.__get_rotate_angle()

            else:
                return 0

        else:
            return int(tmp_angle)

    def run(self) -> None:
        self.__ask()

        if not exists_output_dir():
            missing_output_dir()

        for file in self._pdf_files:
            reader = PdfReader(INPUT_DIR / file)
            writer = PdfWriter()

            for page in reader.pages:
                page.rotate(self.__rotate_angle)
                writer.add_page(page)

            output_file: Path = OUTPUT_DIR / file
            if output_file.is_file(): os.remove(output_file)

            with open(output_file, "wb") as f: writer.write(f)

        print("PDFの回転が完了しました。outputフォルダを確認してください。")
        pause("何かキーを押すとプログラムが終了しoutputフォルダが開きます。")
        print("")
        open_output_dir()