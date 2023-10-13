import tkinter as tk
from misc.shared import UiItems
from widgets.mytext import MyText

from .ui_logic import BindDetailEditorOnModify


def BuildUiDetailEditor(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0.1, relheight=0.9, relwidth=1)

    label = tk.Label(frame, anchor="w", text="Detail")
    label.place(relx=0, rely=0, relheight=0.05, relwidth=1)

    editDetail = MyText(frame)
    editDetail.place(relx=0, rely=0.05, relheight=0.95, relwidth=1)

    BindDetailEditorOnModify(editDetail)
    UiItems.detailEditor = editDetail
