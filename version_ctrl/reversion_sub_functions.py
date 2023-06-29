def UpgradeTo_1_2_0(localInfoDict: dict):
    print("Upgrade local task db -> 1.2.0")
    localInfoDict["ver"] = (1, 2, 0)
    localInfoDict["taskDbDeleted"] = dict()
    localInfoDict["taskOrderDeleted"] = []
    return localInfoDict


# ((target_version, function))
g_UpgradeFuns = (
    ((1,2,0),       UpgradeTo_1_2_0),
)
