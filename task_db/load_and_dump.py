import json
from task_db import TaskDb, TaskDbDel
from logic.bind_func import BindAttrs
from version_ctrl import ReVersionLocalInfo, g_ver


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
        TaskDbDel.taskDb = taskDbDeleted
        TaskDbDel.taskOrder = taskOrderDeleted
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
        "taskDbDeleted": TaskDbDel.taskDb,
        "taskOrderDeleted": TaskDbDel.taskOrder,
        "taskIdCount": BindAttrs.taskIdCount
    }
    with open(path, "w") as f:
        json.dump(toDump, f, indent=2)
