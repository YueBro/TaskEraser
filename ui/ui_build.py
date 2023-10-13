import tkinter as tk
from .ui_panel_left import *
from .ui_panel_right import *


def BuildUi():
    window = tk.Tk()
    window.geometry("900x700")
    window.attributes('-topmost', True)
    BuildUiPanelL(window)
    BuildUiPanelR(window)
