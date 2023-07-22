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


# Will be triggered twice every modification
def ModifyTaskTitle(evnt):
    is_modified = UiItems.editTitle.edit_modified()
    if is_modified:
        print("ModifyTaskTitle", evnt)
        UiItems.editTitle.edit_modified(False)      # Set modified flag to False, so can be retriggered, cuz only trigger once every time editing
        UpdateTaskDbOnModify()


# Will be triggered twice every modification
def ModifyTaskDetail(evnt):
    is_modified = UiItems.editDetail.edit_modified()
    if is_modified:
        print("ModifyTaskDetail", evnt)
        UiItems.editDetail.edit_modified(False)      # Set modified flag to False, so can be retriggered, cuz only trigger once every time editing
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
