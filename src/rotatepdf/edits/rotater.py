import os
from pypdf import PdfReader, PdfWriter
from rotatepdf.log import Log as log
from rotatepdf.edits.editor import Editor
from rotatepdf.files.dir_controls import DirControls as controls

class Rotater(Editor):
    __rotate_angle: int

    def __init__(self, pdf_files: str[]) -> None:
        super().__init__(pdf_files)

    def ask(self) -> bool:
        print("inputフォルダにあるPDFを時計回りに回転させます。")

        tmp_angle: int = self.__get_rotate_angle()
        if tmp_angle == 0:
            log.error("回転角度が無効です。プログラムを終了します。")
            return False

        self.__rotate_angle = tmp_angle

    def __get_rotate_angle(self) -> int:
        tmp_angle: str = input("何度回転させますか？(90, 180, 270): ")

        if tmp_angle not in ["90", "180", "270"]:
            log.warn("回転させる角度は90, 180, 270のいずれかを指定してください。")
            input_continue: str = input("やり直しますか？(Y/N): ")

            if input_continue.lower() == "y":
                return self.__get_rotate_angle()

            else:
                return 0

        else:
            return int(tmp_angle)

    def run(self) -> None:
        for file in self._pdf_files:
            reader = PdfReader(os.path.join(controls.input_dir, file))
            writer = PdfWriter()

            for page in reader.pages:
                page.rotate(self.__rotate_angle)
                writer.add_page(page)

            output_file = os.path.join(controls.output_dir, file)
            if os.path.exists(output_file): os.remove(output_file)

            with open(output_file, "wb") as f: writer.write(f)