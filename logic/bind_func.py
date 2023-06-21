from .logic_func import *


class BindAttrs:
    taskIdCount = 0


def ClickTaskList(evnt):
    print("TaskList", evnt)
    iid = GetSelectedTaskIid()
    if iid != -1:
        DisplayTask(iid)


def ClickAddBut(evnt):
    print("AddBut", evnt)
    
    taskId = BindAttrs.taskIdCount
    BindAttrs.taskIdCount += 1

    TaskDb.StoreTask(taskId, "New Task", "")
    AddTaskList(taskId)
    DisplayTask(taskId)
    UiItems.taskList.selection_set(taskId)  # trigger "ClickTaskList"


def ClickDelBut(evnt):
    print("ClickDelBut", evnt)
    iid = GetSelectedTaskIid()
    if iid != -1:
        DeleteTaskList(iid)
        ClearDisplay()
        TaskDb.RemoveTask(iid)


def ClickRecBut(evnt):
    print("ClickRecBut", evnt)
    taskId, _, _ = TaskDb.RecoverTask()
    if taskId == -1:
        return
    AddTaskList(taskId)
    DisplayTask(taskId)
    UiItems.taskList.selection_set(taskId)


# Will be triggered twice every modification, but leave it for now...
def ModifyTask(evnt):
    UiItems.editTitle.edit_modified(False)      # Set modified flag to False, so can be retriggered,
    UiItems.editDetail.edit_modified(False)     # cuz only trigger once every time editing
    print("ModifyTask", evnt)
    
    iid = GetSelectedTaskIid()
    if iid != -1:
        title, detail = GetDisplayingTask()
        TaskDb.UpdateTask(iid, title, detail)
        UpdateTaskList(iid, title)


def ClickUpBut(evnt):
    print("ClickUpBut", evnt)
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    TaskDb.MoveUp(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)


def ClickDnBut(evnt):
    print("ClickDnBut", evnt)
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    TaskDb.MoveDn(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)
