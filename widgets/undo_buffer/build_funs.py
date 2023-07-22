from .undo_buffer import UndoBuffer


def MakeUndoBuffer(obj):
    assert not hasattr(obj, "undoBuffer")
    obj.undoBuffer = UndoBuffer(undoMaxNum=40)
