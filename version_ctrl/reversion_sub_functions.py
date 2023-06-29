def Upgrade_0_0_0_To_1_2_0(localInfoDict: dict):
    print("task.db  0.0.0 -> 1.2.0")
    localInfoDict["ver"] = (1, 2, 0)
    localInfoDict["taskDbDeleted"] = dict()
    localInfoDict["taskOrderDeleted"] = []
    return localInfoDict, (1, 2, 0)


# ((start_version, function))
g_UpgradeFuns = (
    ((0,0,0),       Upgrade_0_0_0_To_1_2_0),
)
