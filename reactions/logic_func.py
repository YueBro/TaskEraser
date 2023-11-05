from .sub_logic_func import *
from reactions.action_notifier import *

from misc import _ConfigAttr
from misc.shared import UiItems, GlobVals, GlobDbs


def ShowTaskOnUserSelection(evnt: ActEvnt):
    iid = GetTreeviewSelTaskIid()
    if iid != -1:
        if GlobDbs.currDb is GlobDbs.taskDb:
            _ConfigAttr(UiItems.titleEditor, UiItems.detailEditor, state="normal", foreground="black", background="white")
        DisplayTask(iid)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_TREEVIEW_SELECT, ShowTaskOnUserSelection)


def DisableEditorOnEvnt(evnt: ActEvnt):
    DisableEditor()

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_DEL_SELECT_TASK,   DisableEditorOnEvnt)
ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_START_MAIN_LOOP, DisableEditorOnEvnt)


def CreateNewTaskByUser(evnt: ActEvnt):
    if GlobDbs.currDb is not GlobDbs.taskDb:
        print("[CreateNewTaskByUser] rec rejected (currDb != taskDb)")
        return

    taskId = GlobVals.taskIdCount
    GlobVals.taskIdCount += 1

    GlobDbs.currDb.StoreTask(taskId, "New Task", "")
    AddTaskList(taskId, doSelectionSet=True)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_ADD_NEW_TASK, CreateNewTaskByUser)


def DeleteSelectedTaskByUser(evnt: ActEvnt):
    iid = GetTreeviewSelTaskIid()
    if iid == -1:
        return
    DropFromTaskList(iid)
    ClearEditorDisplay()
    idx, title, detail = GlobDbs.currDb.RemoveTask(iid)
    assert idx != -1, "Check your code..."
    if GlobDbs.currDb is GlobDbs.taskDb:
        GlobDbs.taskDbDel.StoreTask(idx, title, detail)
    DisableEditor()

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_DEL_SELECT_TASK, DeleteSelectedTaskByUser)


def RecoverOneDeletedTaskByUser(evnt: ActEvnt):
    if GlobDbs.currDb is not GlobDbs.taskDb:
        print("[RecoverOneDeletedTaskByUser] rec rejected (currDb != taskDb)")
        return

    taskId, title, detail = GlobDbs.taskDbDel.GetLastTask()
    if taskId == -1:
        return
    GlobDbs.taskDbDel.RemoveTask(taskId)
    GlobDbs.taskDb.StoreTask(taskId, title, detail)

    AddTaskList(taskId, doSelectionSet=True)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_REC_ONE_TASK, RecoverOneDeletedTaskByUser)


def UpdateTaskDbOnModify(evnt: ActEvnt):
    iid = GetTreeviewSelTaskIid()
    if iid != -1:
        title, detail = GetDisplayingTask()
        GlobDbs.currDb.UpdateTask(iid, title, detail)
        UpdateTaskList(iid, title)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_EDIT_TITLE,  UpdateTaskDbOnModify)
ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_EDIT_DETAIL, UpdateTaskDbOnModify)


def MoveUpSelectedTask(evnt: ActEvnt):
    iid = GlobVals.selectedIid
    if iid == -1:
        return
    GlobDbs.currDb.MoveUp(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_MOVE_TASK_UP, MoveUpSelectedTask)


def MoveDownSelectedTask(evnt: ActEvnt):
    iid = GlobVals.selectedIid
    if iid == -1:
        return
    GlobDbs.currDb.MoveDn(iid)
    RefreshTaskList()
    UiItems.taskList.selection_set(iid)

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_MOVE_TASK_DN, MoveDownSelectedTask)


def SwitchToBin(evnt: ActEvnt):
    ClearEditorDisplay()
    GlobDbs.currDb = GlobDbs.taskDbDel
    _ConfigAttr(UiItems.addBut, UiItems.recBut, UiItems.upBut, UiItems.dnBut, state="disabled")
    DisableEditor()
    UiItems.delBut.config(text="DEL!!", foreground="red")
    UiItems.binCheckBox.config(foreground="red", activeforeground="red")
    UiItems.menuItems["NewTaskMenuItm"].SetEnable(False)
    UiItems.menuItems["RecTaskMenuItm"].SetEnable(False)
    RefreshTaskList()

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_SWITCH_TO_BIN, SwitchToBin)


def SwitchBackFromBin(evnt: ActEvnt):
    ClearEditorDisplay()
    GlobDbs.currDb = GlobDbs.taskDb
    _ConfigAttr(UiItems.addBut, UiItems.recBut, UiItems.upBut, UiItems.dnBut, state="normal")
    # EnableEditor()
    UiItems.delBut.config(text="DEL", foreground="black")
    UiItems.binCheckBox.config(foreground="black", activeforeground="black")
    UiItems.menuItems["NewTaskMenuItm"].SetEnable(True)
    UiItems.menuItems["RecTaskMenuItm"].SetEnable(True)
    RefreshTaskList()

ActPublisher.RegisterTheToEvntOnly(ACT_EVNT_SWITCH_BACK_FROM_BIN, SwitchBackFromBin)
