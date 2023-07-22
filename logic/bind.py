import tkinter as tk

from ui import UiItems
from .bind_func import *
from widgets.undo_buffer import MakeUndoBuffer


def BindUi():
    UiItems.taskList.bind("<<TreeviewSelect>>", ClickTaskList)
    UiItems.addBut.config(command=ClickAddBut)
    UiItems.delBut.config(command=ClickDelBut)
    UiItems.recBut.config(command=ClickRecBut)
    MakeUndoBuffer(UiItems.editTitle)
    UiItems.editTitle.bind("<<Modified>>", ModifyTaskTitle)
    MakeUndoBuffer(UiItems.editDetail)
    UiItems.editDetail.bind("<<Modified>>", ModifyTaskDetail)
    UiItems.upBut.config(command=ClickUpBut)
    UiItems.dnBut.config(command=ClickDnBut)
    UiItems.binCheckButVal = tk.BooleanVar()
    UiItems.binCheckBut.config(variable=UiItems.binCheckButVal)
    UiItems.binCheckBut.bind("<ButtonRelease>", ClickBinCheckBut)
