import tkinter as tk
from tkinter import ttk


class UiItems:
    taskList: ttk.Treeview = None
    addBut: tk.Button = None
    delBut: tk.Button = None
    upBut: tk.Button = None
    dnBut: tk.Button = None
    editTitle: tk.Text = None
    editDetail: tk.Text = None


def BuildPanelL(root):
    frame = tk.Frame(root, bg="green")
    frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)
    # g_elements["panelL"] = frame
    BuildTaskList(frame)
    BuildModButs(frame)


def BuildPanelR(root):
    frame = tk.Frame(root, bg="cyan")
    frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
    # g_elements["panelR"] = frame
    BuildEditTitle(frame)
    BuildEditDetail(frame)


attrs = (
    {"str": "id", "width": 20},
    {"str": "title", "width": 350},
)
def BuildTaskList(root):
    frame = tk.Frame(root, bg="red")
    frame.place(relx=0, rely=0, relheight=0.9, relwidth=1)

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
    addBut.place(relx=0,    rely=0, relheight=1, relwidth=0.35)
    delBut = tk.Button(frame, text="DEL")
    delBut.place(relx=0.35, rely=0, relheight=1, relwidth=0.35)
    upBut  = tk.Button(frame, text="↑")
    upBut.place (relx=0.7,  rely=0, relheight=1, relwidth=0.15)
    dnBut  = tk.Button(frame, text="↓")
    dnBut.place (relx=0.85, rely=0, relheight=1, relwidth=0.15)

    UiItems.addBut = addBut
    UiItems.delBut = delBut
    UiItems.upBut = upBut
    UiItems.dnBut = dnBut


def BuildEditTitle(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0, relheight=0.1, relwidth=1)

    label = tk.Label(frame, anchor="w", text="Title")
    label.place(relx=0, rely=0, relheight=0.3, relwidth=1)

    editTitle = tk.Text(frame)
    editTitle.place(relx=0, rely=0.3, relheight=0.7, relwidth=1)
    UiItems.editTitle = editTitle

def BuildEditDetail(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0.1, relheight=0.9, relwidth=1)

    label = tk.Label(frame, anchor="w", text="Detail")
    label.place(relx=0, rely=0, relheight=0.05, relwidth=1)

    editDetail = tk.Text(frame)
    editDetail.place(relx=0, rely=0.05, relheight=0.95, relwidth=1)
    UiItems.editDetail = editDetail
