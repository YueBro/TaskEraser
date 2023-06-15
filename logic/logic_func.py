from ui import UiItems


class TaskDb:
    taskDb = dict()     # {id: [title, detail]}
    taskOrder = []

    @classmethod
    def StoreTask(cls, taskId, title, detail):
        if taskId in cls.taskDb:
            raise KeyError(f"Id already exist (id={taskId})")
        cls.taskDb[taskId] = [title, detail]
        cls.taskOrder.append(taskId)

    @classmethod
    def UpdateTask(cls, taskId, title, detail):
        cls.taskDb[taskId] = [title, detail]
    
    @classmethod
    def RemoveTask(cls, taskId):
        cls.taskDb.pop(taskId)
        cls.taskOrder.remove(taskId)
    
    @classmethod
    def GetTask(cls, taskId):
        if taskId in cls.taskDb:
            return cls.taskDb[taskId]
        return None
    
    @classmethod
    def GetIidsInOrder(cls):
        return cls.taskOrder

    @classmethod
    def MoveUp(cls, taskId):
        idx = None
        for i, iid in enumerate(cls.taskOrder):
            if iid == taskId:
                idx = i
                break
        if idx is None:     # 没找到
            return
        
        if idx == (len(cls.taskOrder) - 1):     # 已经到底（添加到order的顺序与显示上下是反的）
            return
        
        cls.taskOrder[i], cls.taskOrder[i+1] = cls.taskOrder[i+1], cls.taskOrder[i]

    @classmethod
    def MoveDn(cls, taskId):
        idx = None
        for i, iid in enumerate(cls.taskOrder):
            if iid == taskId:
                idx = i
                break
        if idx is None:     # 没找到
            return
        
        if idx == 0:        # 已经到顶（添加到order的顺序与显示上下是反的）
            return
        
        cls.taskOrder[i], cls.taskOrder[i-1] = cls.taskOrder[i-1], cls.taskOrder[i]


def AddTaskList(taskId):
    title, _ = TaskDb.GetTask(taskId)
    UiItems.taskList.insert("", 0, iid=taskId, values=(str(taskId), title))


def UpdateTaskList(taskId, title):
    UiItems.taskList.item(taskId, values=(str(taskId), title))
    

def DeleteTaskList(taskId):
    UiItems.taskList.delete(str(taskId))


def ClearTaskList():
    UiItems.taskList.delete(
        *UiItems.taskList.get_children()
    )


def RefreshTaskList():
    ClearTaskList()
    iids = TaskDb.GetIidsInOrder()
    for iid in iids:
        AddTaskList(iid)


def DisplayTask(taskId):
    ClearDisplay()
    title, detail = TaskDb.GetTask(taskId)
    UiItems.editTitle.insert(1.0, title)
    UiItems.editDetail.insert(1.0, detail)


def ClearDisplay():
    UiItems.editTitle.delete("1.0", "end")
    UiItems.editDetail.delete("1.0", "end")


def GetSelectedTaskIid() -> int:
    selectIid = UiItems.taskList.selection()
    if len(selectIid) == 0:
        selectIid = -1
    else:
        selectIid = int(selectIid[0])
    return selectIid


def GetDisplayingTask():
    title = UiItems.editTitle.get("1.0", "end")[:-1]
    detail = UiItems.editDetail.get("1.0", "end")[:-1]
    return title, detail
