from .misc import g_ver

from .reversion_sub_functions import g_upgradeFuns


def ReVersionLocalInfo(localInfoDict: dict):
    for targetVer, func in g_upgradeFuns:
        if GetVersion(localInfoDict) < targetVer:
            fromVer = tuple(localInfoDict['ver'])
            localInfoDict = func(localInfoDict)
            toVer = tuple(localInfoDict['ver'])
            print(f"Upgrade local task db {fromVer} -> {toVer}")

    assert GetVersion(localInfoDict) == g_ver, "Version error, check your code..."
    return localInfoDict


def GetVersion(localInfoDict: dict):
    if "ver" not in localInfoDict:
        return (0, 0, 0)
    else:
        return tuple(localInfoDict["ver"])
