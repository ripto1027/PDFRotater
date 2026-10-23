import sys

from pdfeditor.files.dir_controls import create_input_dir, create_output_dir, open_input_dir
from pdfeditor.utils import pause


def missing_input_dir() -> None:
    print("inputフォルダが見つかりませんでした。")
    input_create_dir: str = input("inputフォルダを作成しますか？(Y/N): ")
    print("")

    if input_create_dir.lower() == "y":
        create_input_dir()
        create_output_dir()
        print("inputファイルを作成しました。")
        print("inputファイルにPDFを入れてもう一度プログラムを実行してください。")
        pause("何かキーを押すとプログラムが終了し、inputフォルダが開かれます。")
        open_input_dir()

    else:
        print("プログラムを終了します。")
        pause()
    
    print("")
    sys.exit()

def missing_output_dir() -> None:
    print("outputフォルダが存在していないため処理を継続できません。outputフォルダを作成します。")
    create_output_dir()
    print("outputフォルダの作成に成功しました。処理を続行します。")
    print("")

def missing_pdf_file() -> None:
    print("inputフォルダにPDFが存在しません。")
    print("inputフォルダにPDFを入れてから再度実行してください。")
    pause("何かキーを押すとプログラムが終了しinputフォルダが開きます。")
    print("")
    open_input_dir()
    sys.exit()