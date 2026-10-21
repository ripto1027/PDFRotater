from enum import Enum
from rotatepdf.edits.editor import Editor
from rotatepdf.edits.rotater import Rotater

class Editors(Enum):
    ROTATE = (0, Rotater, "rotate")

    def __init__(self, index: int, editor_class: type[Editor], command_name: str) -> None:
        self.editor_class = editor_class
        self.command_name = command_name

