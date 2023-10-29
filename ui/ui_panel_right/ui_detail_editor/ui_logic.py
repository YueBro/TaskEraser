from modules.tk_widgets.mytext import MyText
from reactions.action_func import OnModifyTaskDetail


def BindDetailEditorOnModify(editor: MyText):
    assert isinstance(editor, MyText)
    editor.bind("<<Modified>>", OnModifyTaskDetail)
