import tkinter as tk
from misc.shared import UiItems

from .ui_logic import InitializeBinCheckBoxVal, BindBinSwitchBox


def BuildUiBinSwitchBox(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0, relheight=0.05, relwidth=1)

    checkBut = tk.Checkbutton(frame, text="Bin")
    checkBut.pack(side="left")

    InitializeBinCheckBoxVal(checkBut)
    BindBinSwitchBox(checkBut)
    UiItems.binCheckBox = checkBut
