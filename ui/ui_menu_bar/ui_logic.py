import tkinter as tk
from reactions.action_func import (
    OnClickMenuAdd,
    OnClickMenuDel,
    OnClickMenuRec,
    OnClickMenuUp,
    OnClickMenuDn,
)
from modules.menu_topo import MenuTopoNode, MenuTopoSeparator
from typing import Any


MENU_TOPO = \
MenuTopoNode(subNodes=[
    MenuTopoNode(label="Edit", subNodes=[
        MenuTopoNode(label="New Task", accelerator="Ctrl+N", fun=OnClickMenuAdd),
        MenuTopoNode(label="Del Task", accelerator="Ctrl+D", fun=OnClickMenuDel),
        MenuTopoNode(label="Rec Task", accelerator="Ctrl+R", fun=OnClickMenuRec),
        MenuTopoSeparator(),
        MenuTopoNode(label="Move Task Up", accelerator="Ctrl+↑", fun=OnClickMenuUp),
        MenuTopoNode(label="Move Task Down", accelerator="Ctrl+↓", fun=OnClickMenuDn),
    ]),
    MenuTopoNode(label="Reorder", subNodes=[
        MenuTopoSeparator(),
    ]),
])


def SetupMenu(nodeRoot: MenuTopoNode, menuRoot: Any):
    menu = None
    if nodeRoot.HasSubs():
        menu = tk.Menu(menuRoot, tearoff=False)
        nodeRoot.menuWidgt = menu
        if not nodeRoot.IsRoot():
            assert isinstance(menuRoot, tk.Menu)
            menuRoot.add_cascade(label=nodeRoot.label, menu=menu)
        for subNode in nodeRoot.subNodes:
            if isinstance(subNode, MenuTopoSeparator):
                menu.add_separator()
            elif isinstance(subNode, MenuTopoNode):
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
