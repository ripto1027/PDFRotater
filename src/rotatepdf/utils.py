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

def pause() -> None:
    input("Enterキーを押すと終了します。")