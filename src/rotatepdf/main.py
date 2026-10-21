from pypdf import PdfReader, PdfWriter
from rotatepdf.utils import *
import os

# どのPDF編集ツールも何回か回転させるだけでお金を要求してくるのでムカついて作りました。
# ただPDFを回転させるだけのプログラムです。"input"フォルダに入っているPDFを回転させます。
# 回転したPDFは"output"フォルダに出力されます。
def main() -> None:
    base_dir = os.path.join(os.environ["USERPROFILE"], "PDFRotater")

    input_dir = os.path.join(base_dir, "input")
    output_dir = os.path.join(base_dir, "output")

    print("inputフォルダにあるPDFを時計回りに回転させます。")

    rotate_angle = get_rotate_angle()
    if rotate_angle == 0:
        print("回転角度が無効です。プログラムを終了します。")
        pause()
        return

    if not os.path.exists(input_dir):
        missing_input_folder(input_dir, output_dir)
        return

    none_filtered_input_files = os.listdir(input_dir)
    input_files = [file for file in none_filtered_input_files if is_pdf_file(file)]
    if len(input_files) == 0:
        missing_pdf_file(input_dir)
        return
    
    if not os.path.exists(output_dir):
        missing_output_folder(output_dir)

    for file in input_files:        
        reader = PdfReader(os.path.join(input_dir, file))
        writer = PdfWriter()

        for page in reader.pages:
            page.rotate(rotate_angle)
            writer.add_page(page)

        output_file = os.path.join(output_dir, file)
        if os.path.exists(output_file): os.remove(output_file)

        with open(output_file, "wb") as f: writer.write(f)

    print("PDFの回転が完了しました。outputフォルダを確認してください。")
    pause("何かキーを押すとプログラムが終了しoutputフォルダが開きます...")
    os.startfile(output_dir)

if __name__ == "__main__": main()