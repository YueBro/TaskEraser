import tkinter as tk
from reactions.action_func import (
    OnClickAddBut,
    OnClickDelBut,
    OnClickRecBut,
)
from modules.menu_topo import MenuTopoNode, MenuTopoSeparator
from typing import Any


MENU_TOPO = \
MenuTopoNode(subNodes=[
    MenuTopoNode(label="Action", subNodes=[
        MenuTopoNode(label="Add", accelerator="Ctrl+N", fun=OnClickAddBut),
        MenuTopoNode(label="Del", accelerator="Ctrl+D", fun=OnClickDelBut),
        MenuTopoSeparator(),
        MenuTopoNode(label="Rec", accelerator="Ctrl+R", fun=OnClickRecBut),
    ])
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
