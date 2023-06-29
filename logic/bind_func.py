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


# Will be triggered twice every modification, but leave it for now...
def ModifyTask(evnt):
    print("ModifyTask", evnt)
    UiItems.editTitle.edit_modified(False)      # Set modified flag to False, so can be retriggered,
    UiItems.editDetail.edit_modified(False)     # cuz only trigger once every time editing
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
