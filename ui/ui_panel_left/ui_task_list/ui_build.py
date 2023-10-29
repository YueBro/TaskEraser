import tkinter as tk
from tkinter import ttk
from misc.shared import UiItems

from .ui_logic import SetupTaskListBind


attrs = (
    {"str": "id", "width": 20},
    {"str": "title", "width": 350},
)
def BuildUiTaskList(root):
    frame = tk.Frame(root, bg="red")
    frame.place(relx=0, rely=0.05, relheight=0.85, relwidth=1)

    taskList = ttk.Treeview(
        frame,
        columns=tuple(attr["str"] for attr in attrs),
        show="headings",
        selectmode="browse",
    )
    for attr in attrs:
        taskList.column(attr["str"], width=attr["width"])
        taskList.heading(attr["str"], text=attr["str"])
    taskList.place(relx=0, rely=0, relheight=1, relwidth=1)

    SetupTaskListBind(taskList)
    UiItems.taskList = taskList
