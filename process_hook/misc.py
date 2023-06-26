import json
from time import sleep
from logic.logic_func import TaskDb
from logic.bind_func import BindAttrs
import threading as thr
from version_ctrl import ReVersionLocalInfo, g_ver


g_localStoragePth = "tasks.db"
g_autoSavePeriod = 20
g_autoSaveThr: thr.Thread = None
g_autoSaveThrEvnt: thr.Event = thr.Event()


def Load(path):
    try:
        with open(path, "r") as f:
            localInfo = json.load(f)
        localInfo = ReVersionLocalInfo(localInfo)
        taskDb = {int(k):v for k,v in localInfo["taskDb"].items()}
        taskOrder = localInfo["taskOrder"]
        taskDbDeleted = {int(k):v for k,v in localInfo["taskDbDeleted"].items()}
        taskOrderDeleted = localInfo["taskOrderDeleted"]
        taskIdCount = localInfo["taskIdCount"]
        TaskDb.taskDb = taskDb
        TaskDb.taskOrder = taskOrder
        TaskDb.taskDbDeleted = taskDbDeleted
        TaskDb.taskOrderDeleted = taskOrderDeleted
        BindAttrs.taskIdCount = taskIdCount
    except FileNotFoundError:
        print("Warning: local file load fail", "(FileNotFoundError)")
    except json.decoder.JSONDecodeError:
        print("Warning: local file load fail", "(JSONDecodeError)")
    except KeyError:
        print("Warning: local file load fail", "(KeyError)")


def Dump(path):
    toDump = {
        "ver": g_ver,
        "taskDb": TaskDb.taskDb,
        "taskOrder": TaskDb.taskOrder,
        "taskDbDeleted": TaskDb.taskDbDeleted,
        "taskOrderDeleted": TaskDb.taskOrderDeleted,
        "taskIdCount": BindAttrs.taskIdCount
    }
    with open(path, "w") as f:
        json.dump(toDump, f, indent=2)


def StartPeriodicAutoSave():
    global g_autoSaveThr
    g_autoSaveThr = thr.Thread(
        target=PeriodicAutoSave,
        args=(g_autoSaveThrEvnt, g_autoSavePeriod,),
    )
    g_autoSaveThr.start()


def PeriodicAutoSave(evnt, period):
    count = 0
    while not evnt.is_set():
        if count == 0:
            print("PeriodicAutoSave", "(auto save!)")
            Dump(g_localStoragePth)
        count = (count + 1) % period
        sleep(1)
    print("AutoSave terminated")


def StopPeriodicAutoSave():
    if g_autoSaveThr is not None:
        g_autoSaveThrEvnt.set()
        g_autoSaveThr.join()
