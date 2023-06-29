from ui import UiItems
from task_db import TaskDb


def AddTaskList(taskId):
    title, _ = TaskDb.GetTask(taskId)
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
    iids = TaskDb.GetIidsInOrder()
    for iid in iids:
        AddTaskList(iid)


def DisplayTask(taskId):
    ClearDisplay()
    title, detail = TaskDb.GetTask(taskId)
    UiItems.editTitle.insert(1.0, title)
    UiItems.editDetail.insert(1.0, detail)


def ClearDisplay():
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
