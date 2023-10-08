from .sub_logic_func import *
from logic.action_notifier import *

from task_db import TaskDb, TaskDbDel

from misc import _ConfigAttr


def ShowTaskOnUserSelection(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid != -1:
        DisplayTask(iid)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_TREEVIEW_SELECT, ShowTaskOnUserSelection)


def CreateNewTaskByUser(evnt: ActEvnt):
    taskId = Shared.taskIdCount
    Shared.taskIdCount += 1

    Shared.taskDb.StoreTask(taskId, "New Task", "")
    AddTaskList(taskId)
    UiItems.taskList.selection_set(taskId)  # trigger "ClickTaskList"

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_ADD_BUT, CreateNewTaskByUser)


def DeleteSelectedTask(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    DeleteTaskList(iid)
    ClearDisplay()
    idx, title, detail = Shared.taskDb.RemoveTask(iid)
    assert idx != -1, "Check your code..."
    if Shared.taskDb is TaskDb:
        TaskDbDel.StoreTask(idx, title, detail)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_DEL_BUT, DeleteSelectedTask)


def RecoverOneDeletedTask(evnt: ActEvnt):
    taskId, title, detail = TaskDbDel.GetLastTask()
    if taskId == -1:
        return
    TaskDbDel.RemoveTask(taskId)
    TaskDb.StoreTask(taskId, title, detail)

    AddTaskList(taskId)
    UiItems.taskList.selection_set(taskId)  # trigger "ClickTaskList"

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_REC_BUT, RecoverOneDeletedTask)


def UpdateTaskDbOnModify(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid != -1:
        title, detail = GetDisplayingTask()
        Shared.taskDb.UpdateTask(iid, title, detail)
        UpdateTaskList(iid, title)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_EDIT_TITLE,  UpdateTaskDbOnModify)
ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_EDIT_DETAIL, UpdateTaskDbOnModify)


def MoveUpSelectedTask(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    Shared.taskDb.MoveUp(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_UP_BUT, MoveUpSelectedTask)


def MoveDownSelectedTask(evnt: ActEvnt):
    iid = GetSelectedTaskIid()
    if iid == -1:
        return
    Shared.taskDb.MoveDn(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_CLICK_DN_BUT, MoveDownSelectedTask)


def SwitchToBin(evnt: ActEvnt):
    ClearDisplay()
    Shared.taskDb=TaskDbDel
    _ConfigAttr(UiItems.addBut, UiItems.recBut, UiItems.upBut, UiItems.dnBut, state="disabled")
    _ConfigAttr(UiItems.editTitle, UiItems.editDetail, state="disabled", foreground="grey")
    UiItems.delBut.config(text="DEL!!", foreground="red")
    UiItems.binCheckBut.config(foreground="red", activeforeground="red")
    RefreshTaskList()

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_SWITCH_TO_BIN, SwitchToBin)


def SwitchBackFromBin(evnt: ActEvnt):
    ClearDisplay()
    Shared.taskDb=TaskDb
    _ConfigAttr(UiItems.addBut, UiItems.recBut, UiItems.upBut, UiItems.dnBut, state="normal")
    _ConfigAttr(UiItems.editTitle, UiItems.editDetail, state="normal", foreground="black")
    UiItems.delBut.config(text="DEL", foreground="black")
    UiItems.binCheckBut.config(foreground="black", activeforeground="black")
    RefreshTaskList()

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_SWITCH_BACK_FROM_BIN, SwitchBackFromBin)
