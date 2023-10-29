from tkinter import ttk
from reactions.action_func import OnTaskSelect


def SetupTaskListBind(taskList: ttk.Treeview):
    assert isinstance(taskList, ttk.Treeview)
    taskList.bind("<<TreeviewSelect>>", OnTaskSelect)
