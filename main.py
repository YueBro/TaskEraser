import tkinter as tk

from process_hook import ProgramInit, Finish, UiInit
from ui import BuildUi
from logic import BindUi

# import ctypes                                   # No more blurriness! (but with bugs...)
# ctypes.windll.shcore.SetProcessDpiAwareness(1)  # No more blurriness! (but with bugs...)


def main():
    ProgramInit()

    BuildUi()
    BindUi()
    UiInit()
    tk.mainloop()

    Finish()


if __name__ == "__main__":
    main()
