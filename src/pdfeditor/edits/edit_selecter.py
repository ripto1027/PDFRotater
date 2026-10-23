import sys

from pdfeditor.edits.editor import Editor
from pdfeditor.edits.editors import Editors
from pdfeditor.utils import pause

def select_editor() -> type[Editor]:
    print("inputフォルダにあるPDFファイルを編集します。")
    print("操作を以下のリストから選択してください。")
    print("")

    for ed in Editors:
        print(f"{ed.index}. {ed.command_name}")

    print("")
    print("操作の番号または操作名を入力してEnterを押してください。")
    select_word: str = input("操作: ")
    print("")

    optional_editor: type[Editor] | None
    try:
        int_word: int = int(select_word)
        optional_editor = __from_index(int_word)

    except ValueError:
        optional_editor = __from_command_name(select_word)

    if optional_editor == None:
        print(f"{select_word}に該当する操作は見つかりませんでした。")
        input_continue: str = input("もう一度やり直しますか？(Y/N): ")
        print("")

        if input_continue.lower() == "y":
            return select_editor()

        else:
            pause()
            sys.exit()

    return optional_editor

def __from_index(index: int) -> type[Editor] | None:
    return next(
        (ed.editor_type for ed in Editors if ed.index == index),
        None
    )

def __from_command_name(command_name: str) -> type[Editor] | None:
    return next(
        (ed.editor_type for ed in Editors if ed.command_name == command_name),
        None
    )