from .misc import *
from logic.bind_func import *


def ProgramInit():
    LoadAndAssign(g_localStoragePth)
    StartPeriodicAutoSave()


def UiInit():
    iids = TaskDb.GetIidsInOrder()
    for iid in iids:
        AddTaskList(iid)
