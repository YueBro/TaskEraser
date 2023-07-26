from .logic_func import *


def ClickTaskList(evnt):
    print("ClickTaskList", evnt)
    ShowTaskOnUserSelection()


def ClickAddBut():
    print("ClickAddBut")
    CreateNewTaskByUser()


def ClickDelBut():
    print("ClickDelBut")
    DeleteSelectedTask()


def ClickRecBut():
    print("ClickRecBut")
    RecoverOneDeletedTask()


def ModifyTaskTitle(evnt):
    print("ModifyTaskTitle", evnt)
    UpdateTaskDbOnModify()


def ModifyTaskDetail(evnt):
    print("ModifyTaskDetail", evnt)
    UpdateTaskDbOnModify()


def ClickUpBut():
    print("ClickUpBut")
    MoveUpSelectedTask()


def ClickDnBut():
    print("ClickDnBut")
    MoveDownSelectedTask()


def ClickBinCheckBut(evnt):
    currState = UiItems.binCheckButVal.get()
    print("ClickBinCheckBut", evnt, currState)
    SwitchBinState(not currState)
