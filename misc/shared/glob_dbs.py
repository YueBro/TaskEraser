from task_db import TaskDbMgr


class GlobDbs:
    taskDb = TaskDbMgr()
    taskDbDel = TaskDbMgr()

    currDb: TaskDbMgr = None

GlobDbs.currDb = GlobDbs.taskDb
