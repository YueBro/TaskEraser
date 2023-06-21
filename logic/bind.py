from ui import UiItems

from .bind_func import *


def BindUi():
    UiItems.taskList.bind("<<TreeviewSelect>>", ClickTaskList)
    UiItems.addBut.bind("<Button-1>", ClickAddBut)
    UiItems.delBut.bind("<Button-1>", ClickDelBut)
    UiItems.recBut.bind("<Button-1>", ClickRecBut)
    UiItems.editTitle.bind("<<Modified>>", ModifyTask)
    UiItems.editDetail.bind("<<Modified>>", ModifyTask)
    UiItems.upBut.bind("<Button-1>", ClickUpBut)
    UiItems.dnBut.bind("<Button-1>", ClickDnBut)
