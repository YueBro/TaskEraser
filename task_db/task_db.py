class TaskDbMgr():
    taskDb = {}     # {id: [title, detail]}
    taskOrder = []

    def __init__(self) -> None:
        self.taskDb = {}
        self.taskOrder = []

    def ResetDataBase(self):
        self.taskDb = {}     # {id: [title, detail]}
        self.taskOrder = []

    def StoreTask(self, taskId, title, detail):
        if taskId in self.taskOrder:
            raise KeyError(f"Id already exist (id={taskId})")
        self.taskDb[taskId] = [title, detail]
        self.taskOrder.append(taskId)

    def UpdateTask(self, taskId, title, detail):
        if taskId not in self.taskOrder:
            raise KeyError(f"Id not exist (id={taskId})")
        self.taskDb[taskId] = [title, detail]
    
    def RemoveTask(self, taskId):
        if taskId not in self.taskOrder:
            return -1, None, None
        title, detail = self.taskDb.pop(taskId)
        self.taskOrder.remove(taskId)
        return taskId, title, detail

    def GetTask(self, taskId):
        if taskId in self.taskDb:
            return self.taskDb[taskId]
        return None
    
    def GetIidsInOrder(self):
        return [e for e in self.taskOrder]

    def MoveUp(self, taskId):
        idx = None
        for i, iid in enumerate(self.taskOrder):
            if iid == taskId:
                idx = i
                break
        if idx is None:     # 没找到
            return
        
        if idx == (len(self.taskOrder) - 1):     # 已经到底（添加到order的顺序与显示上下是反的）
            return
        
        self.taskOrder[i], self.taskOrder[i+1] = self.taskOrder[i+1], self.taskOrder[i]

    def MoveDn(self, taskId):
        idx = None
        for i, iid in enumerate(self.taskOrder):
            if iid == taskId:
                idx = i
                break
        if idx is None:     # 没找到
            return
        
        if idx == 0:        # 已经到顶（添加到order的顺序与显示上下是反的）
            return
        
        self.taskOrder[i], self.taskOrder[i-1] = self.taskOrder[i-1], self.taskOrder[i]

    def GetLastTask(self):
        if len(self.taskOrder) == 0:
            return -1, None, None
        idx = self.taskOrder[-1]
        title, detail = self.taskDb[idx]
        return idx, title, detail
