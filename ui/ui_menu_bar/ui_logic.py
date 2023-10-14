import tkinter as tk
from reactions.action_func import (
    OnClickAddBut,
    OnClickDelBut,
    OnClickRecBut,
)
from menu_topo import MenuNode, Separator
from typing import Any


MENU_TOPO = \
MenuNode(subNodes=[
    MenuNode(label="Action", subNodes=[
        MenuNode(label="Add", accelerator="Ctrl+N", fun=OnClickAddBut),
        MenuNode(label="Del", accelerator="Ctrl+D", fun=OnClickDelBut),
        Separator(),
        MenuNode(label="Rec", accelerator="Ctrl+R", fun=OnClickRecBut),
    ])
])


def SetupMenu(nodeRoot: MenuNode, menuRoot: Any):
    menu = None
    if nodeRoot.HasSubs():
        menu = tk.Menu(menuRoot, tearoff=False)
        nodeRoot.menuWidgt = menu
        if not nodeRoot.IsRoot():
            assert isinstance(menuRoot, tk.Menu)
            menuRoot.add_cascade(label=nodeRoot.label, menu=menu)
        for subNode in nodeRoot.subNodes:
            if isinstance(subNode, Separator):
                menu.add_separator()
            elif isinstance(subNode, MenuNode):
                SetupMenu(subNode, menu)
            else:
                raise Exception("Unknown node type")
    else:
        assert not nodeRoot.IsRoot()
        assert isinstance(menuRoot, tk.Menu)
        menuRoot.add_command(label=nodeRoot.label,
                             accelerator=nodeRoot.accelerator,
                             command=nodeRoot.fun)
    return menu
