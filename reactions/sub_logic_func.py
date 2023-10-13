from functools import wraps
from misc.shared import UiItems, GlobDbs

from misc import _ConfigAttr


def EnableEditor():
    _ConfigAttr(UiItems.titleEditor, UiItems.detailEditor, state="normal", foreground="black", background="white")


def DisableEditor():
    _ConfigAttr(UiItems.titleEditor, UiItems.detailEditor, state="disabled", foreground="grey", background="#eeeeee")


def _KeepEditorStateDeco(fun):
    @wraps(fun)
    def _fun(*args, **kwargs):
        EnableEditor()
        ret = fun(*args, **kwargs)
        if GlobDbs.currDb is GlobDbs.taskDbDel:
            DisableEditor()
        return ret
    return _fun


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


@_KeepEditorStateDeco
def DisplayTask(taskId):
    title, detail = GlobDbs.currDb.GetTask(taskId)
    UiItems.titleEditor.set_text(title)
    UiItems.detailEditor.set_text(detail)


@_KeepEditorStateDeco
def ClearDisplay():
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
