import os

def get_rotate_angle() -> int:
    input_angle = input("何度回転させますか？(90, 180, 270): ")

    if input_angle not in ["90", "180", "270"]:
        print("回転させる角度は90, 180, 270のいずれかを指定してください。")
        input_continue = input("やり直しますか？(Y/N): ")

        if input_continue.lower() == "y":
            return get_rotate_angle()

        else:
            return 0
        
    else:
        return int(input_angle)

def is_pdf_file(file_name: str) -> bool:
    return file_name.lower().endswith(".pdf")

def pause(message: str = "何かキーを押すと終了します...") -> None:
    input(message)
    print("")

def missing_input_folder(input_dir: str, output_dir: str) -> None:
    print("inputフォルダが存在しません。")
    input_continue = input("inputフォルダを作成しますか？(Y/N): ")

    if input_continue.lower() == "y":
        os.makedirs(input_dir)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print("inputフォルダを作成しました。")
        print("inputフォルダにPDFを入れてから再度実行してください。")
        pause("何かキーを押すとプログラムが終了しinputフォルダが開きます...")
        os.startfile(input_dir)

    else:
        print("プログラムを終了します。")
        pause("何かキーを押すと終了します...")

def missing_output_folder(output_dir: str) -> None:
    print("outputフォルダが存在しないため処理を完遂できません。outputフォルダを作成します。")
    os.makedirs(output_dir)
    print("outputフォルダの作成に成功しました。")

def missing_pdf_file(input_dir: str) -> None:
    print("inputフォルダにPDFが存在しません。")
    print("inputフォルダにPDFを入れてから再度実行してください。")
    input("何かキーを押すとプログラムが終了しinputフォルダが開きます。")
    os.startfile(input_dir)