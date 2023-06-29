from ui import UiItems
from task_db import TaskDb, TaskDbDel

from misc import _ConfigAttr


class Shared:
    taskIdCount = 0
    taskDb = TaskDb


def AddTaskList(taskId):
    title, _ = Shared.taskDb.GetTask(taskId)
    UiItems.taskList.insert("", 0, iid=taskId, values=(str(taskId), title))


def UpdateTaskList(taskId, title):
    UiItems.taskList.item(taskId, values=(str(taskId), title))
    

def DeleteTaskList(taskId):
    UiItems.taskList.delete(str(taskId))


def ClearTaskList():
    UiItems.taskList.delete(
        *UiItems.taskList.get_children()
    )


def RefreshTaskList():
    ClearTaskList()
    iids = Shared.taskDb.GetIidsInOrder()
    for iid in iids:
        AddTaskList(iid)


def DisplayTask(taskId):
    if Shared.taskDb is TaskDbDel:
        _ConfigAttr(UiItems.editTitle, UiItems.editDetail, state="normal")
    ClearDisplay()
    title, detail = Shared.taskDb.GetTask(taskId)
    UiItems.editTitle.insert(1.0, title)
    UiItems.editDetail.insert(1.0, detail)
    if Shared.taskDb is TaskDbDel:
        _ConfigAttr(UiItems.editTitle, UiItems.editDetail, state="disable")


def ClearDisplay():
    _ConfigAttr(UiItems.editTitle, UiItems.editDetail, state="normal")
    UiItems.editTitle.delete("1.0", "end")
    UiItems.editDetail.delete("1.0", "end")


def GetSelectedTaskIid() -> int:
    selectIid = UiItems.taskList.selection()
    if len(selectIid) == 0:
        selectIid = -1
    else:
        selectIid = int(selectIid[0])
    return selectIid


def GetDisplayingTask():
    title = UiItems.editTitle.get("1.0", "end")[:-1]
    detail = UiItems.editDetail.get("1.0", "end")[:-1]
    return title, detail
