from .misc import g_localStoragePth, StartPeriodicAutoSave
from reactions.action_func import RefreshTaskList

from task_db.load_and_dump import Load


def ProgramInit():
    Load(g_localStoragePth)
    StartPeriodicAutoSave()


def UiInit():
    RefreshTaskList()
