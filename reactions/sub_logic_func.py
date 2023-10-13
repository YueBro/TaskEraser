from misc.shared import UiItems
from misc.shared.glob_dbs import *

from misc import _ConfigAttr


def AddTaskList(taskId):
    title, _ = GlobDbs.currDb.GetTask(taskId)
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
    iids = GlobDbs.currDb.GetIidsInOrder()
    for iid in iids:
        AddTaskList(iid)


def DisplayTask(taskId):
    if GlobDbs.currDb is GlobDbs.taskDbDel:
        _ConfigAttr(UiItems.titleEditor, UiItems.detailEditor, state="normal")
    ClearDisplay()
    title, detail = GlobDbs.currDb.GetTask(taskId)
    UiItems.titleEditor.set_text(title)
    UiItems.detailEditor.set_text(detail)
    if GlobDbs.currDb is GlobDbs.taskDbDel:
        _ConfigAttr(UiItems.titleEditor, UiItems.detailEditor, state="disable")


def ClearDisplay():
    _ConfigAttr(UiItems.titleEditor, UiItems.detailEditor, state="normal")
    UiItems.titleEditor.set_text("")
    UiItems.detailEditor.set_text("")


def GetSelectedTaskIid() -> int:
    selectIid = UiItems.taskList.selection()
    if len(selectIid) == 0:
        selectIid = -1
    else:
        selectIid = int(selectIid[0])
    return selectIid


def GetDisplayingTask():
    title = UiItems.titleEditor.get_text()
    detail = UiItems.detailEditor.get_text()
    return title, detail
