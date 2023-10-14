import tkinter as tk
from misc.shared import UiItems
from .ui_logic import MENU_TOPO, SetupMenu


def BuildMenuBar(root: tk.Tk):
    menuBar = SetupMenu(MENU_TOPO, root)
    root.config(menu=menuBar)
    UiItems.menuTopo = MENU_TOPO
