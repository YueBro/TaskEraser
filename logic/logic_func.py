from .sub_logic_func import *

from task_db import TaskDb, TaskDbDel


class BindAttrs:
    taskIdCount = 0


def ShowTaskOnUserSelection():
    iid = GetSelectedTaskIid()
    if iid != -1:
        DisplayTask(iid)


def CreateNewTaskByUser():
    taskId = BindAttrs.taskIdCount
    BindAttrs.taskIdCount += 1

    TaskDb.StoreTask(taskId, "New Task", "")
    AddTaskList(taskId)
    DisplayTask(taskId)
    UiItems.taskList.selection_set(taskId)  # trigger "ClickTaskList"


def DeleteSelectedTask():
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    DeleteTaskList(iid)
    ClearDisplay()
    idx, title, detail = TaskDb.RemoveTask(iid)
    if idx == -1:
        raise("Check your coding...")
    TaskDbDel.StoreTask(idx, title, detail)


def RecoverOneDeletedTask():
    taskId, title, detail = TaskDbDel.GetLastTask()
    if taskId == -1:
        return
    TaskDbDel.RemoveTask(taskId)
    TaskDb.StoreTask(taskId, title, detail)

    AddTaskList(taskId)
    DisplayTask(taskId)
    UiItems.taskList.selection_set(taskId)


def UpdateTaskDbOnModity():
    iid = GetSelectedTaskIid()
    if iid != -1:
        title, detail = GetDisplayingTask()
        TaskDb.UpdateTask(iid, title, detail)
        UpdateTaskList(iid, title)


def MoveUpSelectedTask():
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    TaskDb.MoveUp(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)


def MoveDownSelectedTask():
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    TaskDb.MoveDn(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)
