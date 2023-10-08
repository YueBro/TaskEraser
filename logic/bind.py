import tkinter as tk

from ui import UiItems
from .bind_func import *


def BindUi():
    UiItems.taskList.bind("<<TreeviewSelect>>", OnTaskSelect)
    UiItems.addBut.config(command=OnClickAddBut)
    UiItems.delBut.config(command=OnClickDelBut)
    UiItems.recBut.config(command=OnClickRecBut)
    UiItems.editTitle.bind("<<Modified>>", OnModifyTaskTitle)
    UiItems.editDetail.bind("<<Modified>>", OnModifyTaskDetail)
    UiItems.upBut.config(command=OnClickUpBut)
    UiItems.dnBut.config(command=OnClickDnBut)
    UiItems.binCheckButVal = tk.BooleanVar()
    UiItems.binCheckBut.config(variable=UiItems.binCheckButVal)
    UiItems.binCheckBut.bind("<ButtonRelease>", OnClickBinCheckBut)
