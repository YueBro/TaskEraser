from .misc import *
from logic.bind_func import *


def ProgramInit():
    LoadAndAssign(g_localStoragePth)
    StartPeriodicAutoSave()


def UiInit():
    RefreshTaskList()
