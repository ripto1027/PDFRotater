from pypdf import PdfReader, PdfWriter
from rotatepdf.utils import *
import os, sys

# どのPDF編集ツールも何回か回転させるだけでお金を要求してくるのでムカついて作りました。
# ただPDFを回転させるだけのプログラムです。"input"フォルダに入っているPDFを回転させます。
# 回転したPDFは"output"フォルダに出力されます。
def main() -> None:
    input_dir_path = ""
    output_dir_path = ""
    if getattr(sys, "frozen", False):
        input_dir_path = "input"
        output_dir_path = "output"

    else:
        input_dir_path = "C:\\Document\\.input"
        output_dir_path = "C:\\Document\\.output"

    print("inputフォルダにあるPDFを回転させます。")

    rotate_angle = get_rotate_angle()
    if rotate_angle == 0:
        print("プログラムを終了します。")
        pause()
        return

    if not os.path.exists(input_dir_path):
        print("inputフォルダが存在しません。")
        pause()
        return

    none_filtered_input_dir = os.listdir(input_dir_path)
    input_dir = [file for file in none_filtered_input_dir if is_pdf_file(file)]
    if len(input_dir) == 0:
        print("inputフォルダにファイルが存在しません。")
        pause()
        return
    
    if not os.path.exists(output_dir_path):
        print("outputフォルダが存在しません。")
        pause()
        return

    for file in input_dir:        
        reader = PdfReader(os.path.join(input_dir_path, file))
        writer = PdfWriter()

        for page in reader.pages:
            page.rotate(rotate_angle)
            writer.add_page(page)

        output_file = os.path.join(output_dir_path, file)
        if os.path.exists(output_file): os.remove(output_file)

        with open(output_file, "wb") as f: writer.write(f)

    print("PDFの回転が完了しました。outputフォルダを確認してください。")
    pause()

if __name__ == "__main__":
    main()