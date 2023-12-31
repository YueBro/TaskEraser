import tkinter as tk
from tkinter import ttk

from widgets.mytext import MyText


class UiItems:
    taskList: ttk.Treeview = None
    addBut: tk.Button = None
    delBut: tk.Button = None
    recBut: tk.Button = None
    upBut: tk.Button = None
    dnBut: tk.Button = None
    titleEditor: MyText = None
    detailEditor: MyText = None
    binCheckBoxVal: tk.BooleanVar = None
    binCheckBox: tk.Checkbutton = None
