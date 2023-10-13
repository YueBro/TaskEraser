import tkinter as tk

from process_hook import ProgramInit, Finish, UiInit
from ui import BuildUi

# import ctypes                                   # No more blurriness! (sry Windows...)
# ctypes.windll.shcore.SetProcessDpiAwareness(1)  # No more blurriness! (sry Windows...)


def main():
    ProgramInit()

    BuildUi()
    UiInit()
    tk.mainloop()

    Finish()


if __name__ == "__main__":
    main()
