from .misc import g_localStoragePth, StartPeriodicAutoSave
from logic.bind_func import RefreshTaskList

from task_db.load_and_dump import Load
from task_db import g_taskDb, g_taskDbDel


def ProgramInit():
    Load(g_localStoragePth)
    StartPeriodicAutoSave()
    print(id(g_taskDb.taskDb))
    print(id(g_taskDb.taskOrder))
    print(id(g_taskDbDel.taskDb))
    print(id(g_taskDbDel.taskOrder))


def UiInit():
    RefreshTaskList()
