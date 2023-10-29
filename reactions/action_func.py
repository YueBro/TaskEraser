"""
- Author: Yulin Shen
- Date Created: 
- Last Modified: Oct.29, 2023
- Description:
    The functions below are callbacks of user actions, such as click ADD button, click "add" in menu, ...
"""

from .logic_func import *
from reactions.action_notifier import *
from misc.shared import GlobVals


def OnTaskSelect(evnt):
    print("ClickTaskList", evnt)
    ActPublisher.Publish(ActEvnt(ACT_EVNT_TREEVIEW_SELECT))


def OnClickAddBut():
    print("ClickAddBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_ADD_NEW_TASK))


def OnClickDelBut():
    print("ClickDelBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_DEL_SELECT_TASK))


def OnClickRecBut():
    print("ClickRecBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_REC_ONE_TASK))


def OnModifyTaskTitle(evnt):
    print("ModifyTaskTitle", evnt)
    ActPublisher.Publish(ActEvnt(ACT_EVNT_EDIT_TITLE))


def OnModifyTaskDetail(evnt):
    print("ModifyTaskDetail", evnt)
    ActPublisher.Publish(ActEvnt(ACT_EVNT_EDIT_DETAIL))


def OnClickUpBut():
    print("ClickUpBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_MOVE_TASK_UP))


def OnClickDnBut():
    print("ClickDnBut")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_MOVE_TASK_DN))


def OnClickBinCheckBut(evnt):
    isSwitchToBin = GlobVals.binCheckBoxVal.get() == False
    print("ClickBinCheckBut", evnt, isSwitchToBin)
    if (isSwitchToBin):
        ActPublisher.Publish(ActEvnt(ACT_EVNT_SWITCH_TO_BIN))
    else:
        ActPublisher.Publish(ActEvnt(ACT_EVNT_SWITCH_BACK_FROM_BIN))


def OnClickMenuAdd():
    print("ClickMenuAdd")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_ADD_NEW_TASK))


def OnClickMenuDel():
    print("ClickMenuDel")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_DEL_SELECT_TASK))


def OnClickMenuRec():
    print("ClickMenuRec")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_REC_ONE_TASK))


def OnClickMenuUp():
    print("ClickMenuUp")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_MOVE_TASK_UP))


def OnClickMenuDn():
    print("ClickMenuDn")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_MOVE_TASK_DN))


def OnPressShortCutAdd(evnt):
    print("PressShortCutAdd")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_ADD_NEW_TASK))


def OnPressShortCutDel(evnt):
    print("PressShortCutDel")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_DEL_SELECT_TASK))


def OnPressShortCutRec(evnt):
    print("PressShortCutRec")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_REC_ONE_TASK))


def OnPressShortCutUp(evnt):
    print("PressShortCutUp")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_MOVE_TASK_UP))


def OnPressShortCutDn(evnt):
    print("PressShortCutDn")
    ActPublisher.Publish(ActEvnt(ACT_EVNT_MOVE_TASK_DN))
