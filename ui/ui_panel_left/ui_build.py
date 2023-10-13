import tkinter as tk
from .ui_modify_buttons import *
from .ui_task_list import *
from .ui_top_bubbles import *


def BuildUiPanelL(root):
    frame = tk.Frame(root, bg="green")
    frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)
    BuildUiTopElements(frame)
    BuildUiTaskList(frame)
    BuildUiModifyButtons(frame)
