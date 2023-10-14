import tkinter as tk

from process_hook import ProgramInit, Finish, UiInit
from ui import BuildUi
from reactions.action_notifier import *

# import ctypes                                   # No more blurriness! (sry Windows...)
# ctypes.windll.shcore.SetProcessDpiAwareness(1)  # No more blurriness! (sry Windows...)


def main():
    ProgramInit()

    BuildUi()
    UiInit()

    ActPublisher.Publish(ActEvnt(ACT_EVNT_START_MAIN_LOOP))
    tk.mainloop()

    Finish()


if __name__ == "__main__":
    main()
