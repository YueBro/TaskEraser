from .misc import g_ver

from .reversion_sub_functions import g_UpgradeFuns


def ReVersionLocalInfo(localInfoDict: dict):
    for targetVer, func in g_UpgradeFuns:
        if GetVersion(localInfoDict) < targetVer:
            localInfoDict = func(localInfoDict)

    assert GetVersion(localInfoDict) == g_ver, "Version error, check your code..."
    return localInfoDict


def GetVersion(localInfoDict: dict):
    if "ver" not in localInfoDict:
        return (0, 0, 0)
    else:
        return tuple(localInfoDict["ver"])
