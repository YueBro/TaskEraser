import tkinter as tk
from misc.shared import UiItems

from .ui_logic import BindAddButton, BindDelButton, BindRecButton, BindUpButton, BindDnButton


def BuildUiModifyButtons(root):
    frame = tk.Frame(root)
    frame.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)

    addBut = tk.Button(frame, text="ADD")
    addBut.place(relx=0,     rely=0, relheight=1, relwidth=0.25)
    delBut = tk.Button(frame, text="DEL")
    delBut.place(relx=0.25,  rely=0, relheight=1, relwidth=0.25)
    recBut = tk.Button(frame, text="REC")
    recBut.place(relx=0.5,   rely=0, relheight=1, relwidth=0.25)
    upBut  = tk.Button(frame, text="↑")
    upBut.place (relx=0.75,  rely=0, relheight=1, relwidth=0.125)
    dnBut  = tk.Button(frame, text="↓")
    dnBut.place (relx=0.875, rely=0, relheight=1, relwidth=0.125)

    BindAddButton(addBut)
    UiItems.addBut = addBut
    BindDelButton(delBut)
    UiItems.delBut = delBut
    BindRecButton(recBut)
    UiItems.recBut = recBut
    BindUpButton(upBut)
    UiItems.upBut = upBut
    BindDnButton(dnBut)
    UiItems.dnBut = dnBut
