from .logic_func import *
from reactions.action_notifier import *
from misc.shared.glob_vals import GlobVals


def OnTaskSelect(evnt):
    print("ClickTaskList", evnt)
    ActPublisher.Publish(ActEvnt(ACT_EVNT_TREEVIEW_SELECT))


def OnClickAddBut():
    print("ClickAddBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_CLICK_ADD_BUT))


def OnClickDelBut():
    print("ClickDelBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_CLICK_DEL_BUT))


def OnClickRecBut():
    print("ClickRecBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_CLICK_REC_BUT))


def OnModifyTaskTitle(evnt):
    print("ModifyTaskTitle", evnt)
    ActPublisher.Publish(ActEvnt(ACT_EVNT_EDIT_TITLE))


def OnModifyTaskDetail(evnt):
    print("ModifyTaskDetail", evnt)
    ActPublisher.Publish(ActEvnt(ACT_EVNT_EDIT_DETAIL))


def OnClickUpBut():
    print("ClickUpBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_CLICK_UP_BUT))


def OnClickDnBut():
    print("ClickDnBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_CLICK_DN_BUT))


def OnClickBinCheckBut(evnt):
    isSwitchToBin = GlobVals.binCheckBoxVal.get() == False
    print("ClickBinCheckBut", evnt, isSwitchToBin)
    if (isSwitchToBin):
        ActPublisher.Publish(ActEvnt(ACT_EVNT_SWITCH_TO_BIN))
    else:
        ActPublisher.Publish(ActEvnt(ACT_EVNT_SWITCH_BACK_FROM_BIN))
