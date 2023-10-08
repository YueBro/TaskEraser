import tkinter as tk
from tkinter import ttk

from widgets.mytext import MyText


class UiItems:
    taskList: ttk.Treeview = None
    addBut: tk.Button = None
    delBut: tk.Button = None
    recBut: tk.Button = None
    upBut: tk.Button = None
    dnBut: tk.Button = None
    editTitle: MyText = None
    editDetail: MyText = None
    binCheckButVal: tk.BooleanVar = None
    binCheckBut: tk.Checkbutton = None


def BuildPanelL(root):
    frame = tk.Frame(root, bg="green")
    frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)
    BuildTopBubbles(frame)
    BuildTaskList(frame)
    BuildModButs(frame)


def BuildPanelR(root):
    frame = tk.Frame(root, bg="cyan")
    frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
    BuildEditTitle(frame)
    BuildEditDetail(frame)


def BuildTopBubbles(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0, relheight=0.05, relwidth=1)

    checkBut = tk.Checkbutton(frame, text="Bin")
    checkBut.pack(side="left")

    UiItems.binCheckBut = checkBut


attrs = (
    {"str": "id", "width": 20},
    {"str": "title", "width": 350},
)
def BuildTaskList(root):
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
    UiItems.taskList = taskList


def BuildModButs(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)

    addBut = tk.Button(frame, text="ADD")
    addBut.place(relx=0,     rely=0, relheight=1, relwidth=0.25)
    delBut = tk.Button(frame, text="DEL")
    delBut.place(relx=0.25,  rely=0, relheight=1, relwidth=0.25)
    recBut = tk.Button(frame, text="REC")
    recBut.place(relx=0.5,   rely=0, relheight=1, relwidth=0.25)
    upBut  = tk.Button(frame, text="↑")
    upBut.place (relx=0.75,  rely=0, relheight=1, relwidth=0.125)
    dnBut  = tk.Button(frame, text="↓")
    dnBut.place (relx=0.875, rely=0, relheight=1, relwidth=0.125)

    UiItems.addBut = addBut
    UiItems.delBut = delBut
    UiItems.recBut = recBut
    UiItems.upBut = upBut
    UiItems.dnBut = dnBut


def BuildEditTitle(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0, relheight=0.1, relwidth=1)

    label = tk.Label(frame, anchor="w", text="Title")
    label.place(relx=0, rely=0, relheight=0.3, relwidth=1)

    editTitle = MyText(frame)
    editTitle.place(relx=0, rely=0.3, relheight=0.7, relwidth=1)
    UiItems.editTitle = editTitle

def BuildEditDetail(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0.1, relheight=0.9, relwidth=1)

    label = tk.Label(frame, anchor="w", text="Detail")
    label.place(relx=0, rely=0, relheight=0.05, relwidth=1)

    editDetail = MyText(frame)
    editDetail.place(relx=0, rely=0.05, relheight=0.95, relwidth=1)
    UiItems.editDetail = editDetail
