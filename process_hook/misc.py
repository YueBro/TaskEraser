import json
from logic.logic_func import TaskDb
from logic.bind_func import BindAttrs


g_localStoragePth = "tasks.db"


def LoadAndAssign(path):
    try:
        with open(path, "r") as f:
            localInfo = json.load(f)
            taskDb = {int(k):v for k,v in localInfo["taskDb"].items()}
            taskOrder = localInfo["taskOrder"]
            taskIdCount = localInfo["taskIdCount"]
        TaskDb.taskDb = taskDb
        TaskDb.taskOrder = taskOrder
        BindAttrs.taskIdCount = taskIdCount
    except FileNotFoundError:
        print("Warning: local file load fail", "(FileNotFoundError)")
    except json.decoder.JSONDecodeError:
        print("Warning: local file load fail", "(JSONDecodeError)")
    except KeyError:
        print("Warning: local file load fail", "(KeyError)")

def Dump(path):
    toDump = {
        "taskDb": TaskDb.taskDb,
        "taskOrder": TaskDb.taskOrder,
        "taskIdCount": BindAttrs.taskIdCount
    }
    with open(path, "w") as f:
        json.dump(toDump, f)
