class _TaskDbBase:
    taskDb = dict()     # {id: [title, detail]}
    taskOrder = []

    @classmethod
    def StoreTask(cls, taskId, title, detail):
        if taskId in cls.taskOrder:
            raise KeyError(f"Id already exist (id={taskId})")
        cls.taskDb[taskId] = [title, detail]
        cls.taskOrder.append(taskId)

    @classmethod
    def UpdateTask(cls, taskId, title, detail):
        if taskId not in cls.taskOrder:
            raise KeyError(f"Id not exist (id={taskId})")
        cls.taskDb[taskId] = [title, detail]
    
    @classmethod
    def RemoveTask(cls, taskId):
        if taskId not in cls.taskOrder:
            return -1, None, None
        title, detail = cls.taskDb.pop(taskId)
        cls.taskOrder.remove(taskId)
        return taskId, title, detail

    @classmethod
    def GetTask(cls, taskId):
        if taskId in cls.taskDb:
            return cls.taskDb[taskId]
        return None
    
    @classmethod
    def GetIidsInOrder(cls):
        return [e for e in cls.taskOrder]


class TaskDb(_TaskDbBase):
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


class TaskDbDel(_TaskDbBase):
    @classmethod
    def GetLastTask(cls):
        if len(cls.taskOrder) == 0:
            return -1, None, None
        idx = cls.taskOrder[-1]
        title, detail = cls.taskDb[idx]
        return idx, title, detail
