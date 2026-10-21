import os
from typing import Final
from rotatepdf.utils import pause
from rotatepdf.log import Log as log

class DirControls:
    base_dir: Final[str] = os.path.join(os.environ["USERPROFILE"], "PDFRotater")
    input_dir: Final[str] = os.path.join(base_dir, "input")
    output_dir: Final[str] = os.path.join(base_dir, "output")

    @staticmethod
    def exists_input_dir() -> bool:
        return os.path.exists(DirControls.input_dir)

    @staticmethod
    def exists_output_dir() -> bool:
        return os.path.exists(DirControls.output_dir)

    @staticmethod
    def create_input_dir() -> None:
        os.makedirs(DirControls.input_dir, exist_ok=True)

    @staticmethod
    def create_output_dir() -> None:
        os.makedirs(DirControls.output_dir, exist_ok=True)

    @staticmethod
    def open_input_dir() -> None:
        os.startfile(DirControls.input_dir)

    @staticmethod
    def open_output_dir() -> None:
        os.startfile(DirControls.output_dir)

    @staticmethod
    def missing_input_dir() -> None:
        log.error("inputフォルダが見つかりませんでした。")
        input_create_dir: str = input("inputフォルダを作成しますか？(Y/N): ")
        print("")

        if input_create_dir.lower() == "y":
            DirControls.create_input_dir()
            DirControls.create_output_dir()
            log.info("inputファイルを作成しました。")
            log.info("inputファイルにPDFを入れてもう一度プログラムを実行してください。")
            pause("何かキーを押すとプログラムが終了し、inputフォルダが開かれます。")
            os.startfile(DirControls.input_dir)

        else:
            log.info("プログラムを終了します。")
            pause()

        exit()

    @staticmethod
    def missing_output_dir() -> None:
        log.warn("outputフォルダが存在していないため処理を継続できません。outputフォルダを作成します。")
        DirControls.create_output_dir()
        log.info("outputフォルダの作成に成功しました。処理を続行します。")

    @staticmethod
    def missing_pdf_file() -> None:
        log.error("inputフォルダにPDFが存在しません。")
        log.error("inputフォルダにPDFを入れてから再度実行してください。")
        pause("何かキーを押すとプログラムが終了しinputフォルダが開きます。")
        os.startfile(input_dir)
        exit()

    