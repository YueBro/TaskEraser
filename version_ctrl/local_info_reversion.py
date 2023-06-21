from .misc import g_ver


def ReVersionLocalInfo(localInfoDict: dict):
    ver = GetVersion(localInfoDict)
    if ver < (1, 2, 0):
        localInfoDict, ver = Upgrade_0_0_0_To_1_2_0(localInfoDict)
    assert ver == g_ver, "Version error, check your code..."
    return localInfoDict


def GetVersion(localInfoDict: dict):
    if "ver" not in localInfoDict:
        return (0, 0, 0)
    else:
        return tuple(localInfoDict["ver"])


def Upgrade_0_0_0_To_1_2_0(localInfoDict: dict):
    localInfoDict["ver"] = (1, 2, 0)
    localInfoDict["taskDbDeleted"] = []
    return localInfoDict, (1, 2, 0)
