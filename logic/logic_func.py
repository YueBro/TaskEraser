from .sub_logic_func import *

from task_db import TaskDb, TaskDbDel

from misc import _ConfigAttr


def ShowTaskOnUserSelection():
    iid = GetSelectedTaskIid()
    if iid != -1:
        DisplayTask(iid)


def CreateNewTaskByUser():
    taskId = Shared.taskIdCount
    Shared.taskIdCount += 1

    Shared.taskDb.StoreTask(taskId, "New Task", "")
    AddTaskList(taskId)
    UiItems.taskList.selection_set(taskId)  # trigger "ClickTaskList"


def DeleteSelectedTask():
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    DeleteTaskList(iid)
    ClearDisplay()
    idx, title, detail = Shared.taskDb.RemoveTask(iid)
    assert idx != -1, "Check your code..."
    if Shared.taskDb is TaskDb:
        TaskDbDel.StoreTask(idx, title, detail)


def RecoverOneDeletedTask():
    taskId, title, detail = TaskDbDel.GetLastTask()
    if taskId == -1:
        return
    TaskDbDel.RemoveTask(taskId)
    TaskDb.StoreTask(taskId, title, detail)

    AddTaskList(taskId)
    UiItems.taskList.selection_set(taskId)  # trigger "ClickTaskList"


def UpdateTaskDbOnModify():
    iid = GetSelectedTaskIid()
    if iid != -1:
        title, detail = GetDisplayingTask()
        Shared.taskDb.UpdateTask(iid, title, detail)
        UpdateTaskList(iid, title)


def MoveUpSelectedTask():
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    Shared.taskDb.MoveUp(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)


def MoveDownSelectedTask():
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    Shared.taskDb.MoveDn(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)


def SwitchBinState(toBin):
    ClearDisplay()
    if toBin is True:
        Shared.taskDb=TaskDbDel
        _ConfigAttr(UiItems.addBut, UiItems.recBut, UiItems.upBut, UiItems.dnBut, state="disabled")
        _ConfigAttr(UiItems.editTitle, UiItems.editDetail, state="disabled", foreground="grey")
        UiItems.delBut.config(text="DEL!!", foreground="red")
        UiItems.binCheckBut.config(foreground="red")
    else:
        Shared.taskDb=TaskDb
        _ConfigAttr(UiItems.addBut, UiItems.recBut, UiItems.upBut, UiItems.dnBut, state="normal")
        _ConfigAttr(UiItems.editTitle, UiItems.editDetail, state="normal", foreground="black")
        UiItems.delBut.config(text="DEL", foreground="black")
        UiItems.binCheckBut.config(foreground="black")
    RefreshTaskList()
