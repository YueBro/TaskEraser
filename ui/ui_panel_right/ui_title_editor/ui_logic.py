from widgets.mytext import MyText
from reactions.action_func import OnModifyTaskTitle


def BindTitleEditorOnModify(editor: MyText):
    assert isinstance(editor, MyText)
    editor.bind("<<Modified>>", OnModifyTaskTitle)
