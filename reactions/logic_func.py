from .sub_logic_func import *
from reactions.action_notifier import *

from misc import _ConfigAttr
from misc.shared import UiItems, GlobVals
from misc.shared.glob_dbs import *


def ShowTaskOnUserSelection(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid != -1:
        DisplayTask(iid)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_TREEVIEW_SELECT, ShowTaskOnUserSelection)


def CreateNewTaskByUser(evnt: ActEvnt):
    taskId = GlobVals.taskIdCount
    GlobVals.taskIdCount += 1

    GlobDbs.currDb.StoreTask(taskId, "New Task", "")
    AddTaskList(taskId)
    UiItems.taskList.selection_set(taskId)  # trigger "ClickTaskList"

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_ADD_BUT, CreateNewTaskByUser)


def DeleteSelectedTask(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    DeleteTaskList(iid)
    ClearDisplay()
    idx, title, detail = GlobDbs.currDb.RemoveTask(iid)
    assert idx != -1, "Check your code..."
    if GlobDbs.currDb is GlobDbs.taskDb:
        GlobDbs.taskDbDel.StoreTask(idx, title, detail)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_DEL_BUT, DeleteSelectedTask)


def RecoverOneDeletedTask(evnt: ActEvnt):
    taskId, title, detail = GlobDbs.taskDbDel.GetLastTask()
    if taskId == -1:
        return
    GlobDbs.taskDbDel.RemoveTask(taskId)
    GlobDbs.taskDb.StoreTask(taskId, title, detail)

    AddTaskList(taskId)
    UiItems.taskList.selection_set(taskId)  # trigger "ClickTaskList"

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_REC_BUT, RecoverOneDeletedTask)


def UpdateTaskDbOnModify(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid != -1:
        title, detail = GetDisplayingTask()
        GlobDbs.currDb.UpdateTask(iid, title, detail)
        UpdateTaskList(iid, title)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_EDIT_TITLE,  UpdateTaskDbOnModify)
ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_EDIT_DETAIL, UpdateTaskDbOnModify)


def MoveUpSelectedTask(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    GlobDbs.currDb.MoveUp(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_UP_BUT, MoveUpSelectedTask)


def MoveDownSelectedTask(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    GlobDbs.currDb.MoveDn(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_DN_BUT, MoveDownSelectedTask)


def SwitchToBin(evnt: ActEvnt):
    ClearDisplay()
    GlobDbs.currDb = GlobDbs.taskDbDel
    _ConfigAttr(UiItems.addBut, UiItems.recBut, UiItems.upBut, UiItems.dnBut, state="disabled")
    _ConfigAttr(UiItems.titleEditor, UiItems.detailEditor, state="disabled", foreground="grey")
    UiItems.delBut.config(text="DEL!!", foreground="red")
    UiItems.binCheckBox.config(foreground="red", activeforeground="red")
    RefreshTaskList()

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_SWITCH_TO_BIN, SwitchToBin)


def SwitchBackFromBin(evnt: ActEvnt):
    ClearDisplay()
    GlobDbs.currDb = GlobDbs.taskDb
    _ConfigAttr(UiItems.addBut, UiItems.recBut, UiItems.upBut, UiItems.dnBut, state="normal")
    _ConfigAttr(UiItems.titleEditor, UiItems.detailEditor, state="normal", foreground="black")
    UiItems.delBut.config(text="DEL", foreground="black")
    UiItems.binCheckBox.config(foreground="black", activeforeground="black")
    RefreshTaskList()

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_SWITCH_BACK_FROM_BIN, SwitchBackFromBin)
