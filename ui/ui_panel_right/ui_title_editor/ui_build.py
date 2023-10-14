import tkinter as tk
from misc.shared import UiItems
from widgets.mytext import MyText

from .ui_logic import BindTitleEditorOnModify


def BuildUiTitleEditor(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0, relheight=0.1, relwidth=1)

    label = tk.Label(frame, anchor="w", text="Title")
    label.place(relx=0, rely=0, relheight=0.3, relwidth=1)

    editTitle = MyText(frame)
    editTitle.place(relx=0, rely=0.3, relheight=0.7, relwidth=1)

    BindTitleEditorOnModify(editTitle)
    UiItems.titleEditor = editTitle
