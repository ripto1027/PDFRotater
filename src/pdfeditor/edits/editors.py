from enum import Enum
from pdfeditor.edits.editor import Editor
from pdfeditor.edits.rotater import Rotater

class Editors(Enum):
    ROTATE = (Rotater, 1, "回転")

    def __init__(self, editor_type: type[Editor], index: int, command_name: str) -> None:
        self.editor_type = editor_type
        self.index = index
        self.command_name = command_name