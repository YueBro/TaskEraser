import tkinter as tk

from ui import UiItems

from .bind_func import *


def BindUi():
    UiItems.taskList.bind("<<TreeviewSelect>>", ClickTaskList)
    UiItems.addBut.config(command=ClickAddBut)
    UiItems.delBut.config(command=ClickDelBut)
    UiItems.recBut.config(command=ClickRecBut)
    UiItems.editTitle.bind("<<Modified>>", ModifyTask)
    UiItems.editDetail.bind("<<Modified>>", ModifyTask)
    UiItems.upBut.config(command=ClickUpBut)
    UiItems.dnBut.config(command=ClickDnBut)
    UiItems.binCheckButVal = tk.BooleanVar()
    UiItems.binCheckBut.config(variable=UiItems.binCheckButVal)
    UiItems.binCheckBut.bind("<ButtonRelease>", ClickBinCheckBut)
