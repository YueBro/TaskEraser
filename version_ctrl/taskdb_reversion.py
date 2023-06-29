from .misc import g_ver

from .reversion_sub_functions import g_UpgradeFuns


def ReVersionLocalInfo(localInfoDict: dict):
    ver = GetVersion(localInfoDict)

    for startVer, func in g_UpgradeFuns:
        if ver == startVer:
            localInfoDict, ver = func(localInfoDict)

    assert ver == g_ver, "Version error, check your code..."
    return localInfoDict


def GetVersion(localInfoDict: dict):
    if "ver" not in localInfoDict:
        return (0, 0, 0)
    else:
        return tuple(localInfoDict["ver"])
