import tkinter as tk
from reactions.action_func import OnClickBinCheckBut

from misc.shared.glob_vals import GlobVals


def InitializeBinCheckBoxVal(binBox: tk.Checkbutton):
    assert isinstance(binBox, tk.Checkbutton)
    GlobVals.binCheckBoxVal = tk.BooleanVar()
    binBox.config(variable=GlobVals.binCheckBoxVal)


def BindBinSwitchBox(binBox: tk.Checkbutton):
    assert isinstance(binBox, tk.Checkbutton)
    binBox.bind("<ButtonRelease>", OnClickBinCheckBut)
