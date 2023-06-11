import tkinter as tk

from process_hook import ProgramInit, Finish, UiInit
from ui import BuildUi
from logic import BindUi


def main():
    ProgramInit()

    BuildUi()
    BindUi()
    UiInit()
    tk.mainloop()

    Finish()


if __name__ == "__main__":
    main()
