import tkinter as tk
from .ui_detail_editor import *
from .ui_title_editor import *


def BuildUiPanelR(root):
    frame = tk.Frame(root, bg="cyan")
    frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
    BuildUiTitleEditor(frame)
    BuildUiDetailEditor(frame)
