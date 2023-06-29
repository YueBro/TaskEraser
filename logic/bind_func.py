from .logic_func import *


def ClickTaskList(evnt):
    print("TaskList", evnt)
    ShowTaskOnUserSelection()


def ClickAddBut(evnt):
    print("AddBut", evnt)
    CreateNewTaskByUser()


def ClickDelBut(evnt):
    print("ClickDelBut", evnt)
    DeleteSelectedTask()


def ClickRecBut(evnt):
    print("ClickRecBut", evnt)
    RecoverOneDeletedTask()


# Will be triggered twice every modification, but leave it for now...
def ModifyTask(evnt):
    print("ModifyTask", evnt)
    UiItems.editTitle.edit_modified(False)      # Set modified flag to False, so can be retriggered,
    UiItems.editDetail.edit_modified(False)     # cuz only trigger once every time editing
    UpdateTaskDbOnModity()


def ClickUpBut(evnt):
    print("ClickUpBut", evnt)
    MoveUpSelectedTask()


def ClickDnBut(evnt):
    print("ClickDnBut", evnt)
    MoveDownSelectedTask()
