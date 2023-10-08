import tkinter as tk

from .build_elements import *


def BuildUi():
    global UiItems
    window = BuildWindow()
    BuildPanelL(window)
    BuildPanelR(window)


def BuildWindow():
    window = tk.Tk()
    window.geometry("900x700")
    window.attributes('-topmost', True)
    return window
