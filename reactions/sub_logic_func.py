from functools import wraps
from misc.shared import UiItems, GlobDbs, GlobVals

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


def AddTaskList(taskId, doSelectionSet = False):
    title, _ = GlobDbs.currDb.GetTask(taskId)
    UiItems.taskList.insert("", 0, iid=taskId, values=(str(taskId), title))
    if doSelectionSet:
        UiItems.taskList.selection_set(taskId)  # trigger "ClickTaskList"
        GlobVals.selectedIid = taskId


def UpdateTaskList(taskId, title):
    UiItems.taskList.item(taskId, values=(str(taskId), title))
    

def DropFromTaskList(taskId):
    UiItems.taskList.delete(str(taskId))
    if taskId == GlobVals.selectedIid:
        GlobVals.selectedIid = -1


def ClearTaskList():
    UiItems.taskList.delete(
        *UiItems.taskList.get_children()
    )
    GlobVals.selectedIid = -1


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
def ClearEditorDisplay():
    UiItems.titleEditor.set_text("")
    UiItems.detailEditor.set_text("")


def GetTreeviewSelTaskIid() -> int:
    selectIid = UiItems.taskList.selection()
    if len(selectIid) == 0:
        selectIid = -1
    else:
        selectIid = int(selectIid[0])
    GlobVals.selectedIid = selectIid
    return selectIid


def GetDisplayingTask():
    title = UiItems.titleEditor.get_text()
    detail = UiItems.detailEditor.get_text()
    return title, detail
