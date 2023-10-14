import os
import shutil
import json
from misc.shared import GlobVals, GlobDbs
from version_ctrl import ReVersionLocalInfo, g_ver


def _GetFileDirAndNameAndSuffix(pth):
    _fileSplit = os.path.basename(pth).split(".")
    if (len(_fileSplit) == 1):
        fileName = _fileSplit[0]
        fileSufx = ""
    else:
        fileName = ".".join(_fileSplit[:-1])
        fileSufx = "." + _fileSplit[-1]
    fileDir = os.path.dirname(pth)
    return fileDir, fileName, fileSufx


def _MakeCopy(pth):
    if not os.path.exists(pth):
        return
    
    _dir, _name, _sufx = _GetFileDirAndNameAndSuffix(pth)
    
    count = 1
    newPth = os.path.join(_dir, _name + " copy" + _sufx)
    while (os.path.exists(newPth)):
        count += 1
        newPth = os.path.join(_dir, _name + f" copy{count}" + _sufx)
    print("_MakeCopy:", pth, "->", newPth)
    shutil.copy(pth, newPth)


def Load(path):
    try:
        with open(path, "r") as f:
            localInfo = json.load(f)
        localInfo = ReVersionLocalInfo(localInfo)
        taskDb = {int(k): v for k,v in localInfo["taskDb"].items()}
        taskOrder = localInfo["taskOrder"]
        taskDbDeleted = {int(k): v for k,v in localInfo["taskDbDeleted"].items()}
        taskOrderDeleted = localInfo["taskOrderDeleted"]
        taskIdCount = localInfo["taskIdCount"]
        GlobDbs.taskDb.taskDb = taskDb
        GlobDbs.taskDb.taskOrder = taskOrder
        GlobDbs.taskDbDel.taskDb = taskDbDeleted
        GlobDbs.taskDbDel.taskOrder = taskOrderDeleted
        GlobVals.taskIdCount = taskIdCount
    except FileNotFoundError:
        print("Warning: local file load fail", "(FileNotFoundError)")
        _MakeCopy(path)
    except json.decoder.JSONDecodeError:
        print("Warning: local file load fail", "(JSONDecodeError)")
        _MakeCopy(path)
    except KeyError:
        print("Warning: local file load fail", "(KeyError)")
        _MakeCopy(path)


def Dump(path):
    toDump = {
        "ver": g_ver,
        "taskDb": GlobDbs.taskDb.taskDb,
        "taskOrder": GlobDbs.taskDb.taskOrder,
        "taskDbDeleted": GlobDbs.taskDbDel.taskDb,
        "taskOrderDeleted": GlobDbs.taskDbDel.taskOrder,
        "taskIdCount": GlobVals.taskIdCount
    }
    with open(path, "w") as f:
        json.dump(toDump, f, indent=2)
