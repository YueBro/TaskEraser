from .misc import *
from logic.bind_func import *


def ProgramInit():
    Load(g_localStoragePth)
    StartPeriodicAutoSave()


def UiInit():
    RefreshTaskList()
