import os
import tkinter as tk
from reactions.action_func import (
    OnPressShortCutAdd,
    OnPressShortCutDel,
    OnPressShortCutRec,
    OnPressShortCutUp,
    OnPressShortCutDn,
)


def _DummyFun(evnt):
    pass


def SetupTopLevelShortCuts(root: tk.Tk):
    assert isinstance(root, tk.Tk)
    root.bind("<Control-n>", OnPressShortCutAdd)
    root.bind("<Control-N>", OnPressShortCutAdd)
    root.bind("<Control-Shift-n>", _DummyFun)   # Override problem of <Control-Shift-n> == <Control-N>
    root.bind("<Control-Shift-N>", _DummyFun)   # Override problem of <Control-Shift-N> == <Control-n>

    root.bind("<Control-d>", OnPressShortCutDel)
    root.bind("<Control-D>", OnPressShortCutDel)
    root.bind("<Control-Shift-d>", _DummyFun)   # Override problem of <Control-Shift-d> == <Control-D>
    root.bind("<Control-Shift-D>", _DummyFun)   # Override problem of <Control-Shift-D> == <Control-d>

    root.bind("<Control-r>", OnPressShortCutRec)
    root.bind("<Control-R>", OnPressShortCutRec)
    root.bind("<Control-Shift-r>", _DummyFun)   # Override problem of <Control-Shift-r> == <Control-R>
    root.bind("<Control-Shift-R>", _DummyFun)   # Override problem of <Control-Shift-R> == <Control-r>

    root.bind("<Control-Up>", OnPressShortCutUp)
    root.bind("<Control-Down>", OnPressShortCutDn)


def SetWindowAttributes(root: tk.Tk):
    title = "TaskEraser (DEVELOP VERSION)" if (os.path.isfile("./DEVELOPING")) \
            else "TaskEraser"
    root.title(title)
