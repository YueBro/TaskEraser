import tkinter as tk
from .ui_menu_bar import *
from .ui_panel_left import *
from .ui_panel_right import *

from .ui_logic import SetupTopLevelShortCuts


def BuildUi():
    window = tk.Tk()
    window.geometry("900x700")
    window.attributes('-topmost', True)
    BuildMenuBar(window)
    BuildUiPanelL(window)
    BuildUiPanelR(window)

    SetupTopLevelShortCuts(window)
