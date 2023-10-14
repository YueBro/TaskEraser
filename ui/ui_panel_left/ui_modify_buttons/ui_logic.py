import tkinter as tk
from reactions.action_func import OnClickAddBut, OnClickDelBut, OnClickRecBut, OnClickUpBut, OnClickDnBut


def BindAddButton(button: tk.Button):
    assert isinstance(button, tk.Button)
    button.config(command=OnClickAddBut)


def BindDelButton(button: tk.Button):
    assert isinstance(button, tk.Button)
    button.config(command=OnClickDelBut)


def BindRecButton(button: tk.Button):
    assert isinstance(button, tk.Button)
    button.config(command=OnClickRecBut)

def BindUpButton(button: tk.Button):
    assert isinstance(button, tk.Button)
    button.config(command=OnClickUpBut)


def BindDnButton(button: tk.Button):
    assert isinstance(button, tk.Button)
    button.config(command=OnClickDnBut)
