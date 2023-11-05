import tkinter as tk
from reactions.action_func import (
    OnClickMenuAdd,
    OnClickMenuDel,
    OnClickMenuRec,
    OnClickMenuUp,
    OnClickMenuDn,
)
from modules.menu_topo import MenuTopoNode, MenuTopoSeparator
from misc.shared import UiItems

from typing import Any


def _AddToUiitems(key, nodeObj: MenuTopoNode):
    if key in UiItems.menuItems:
        raise Exception(f"key ({key}) already exists!")
    UiItems.menuItems[key] = nodeObj


MENU_TOPO = \
MenuTopoNode(subNodes=[
    MenuTopoNode(label="Edit", subNodes=[
        MenuTopoNode(label="New Task", accelerator="Ctrl+N", fun=OnClickMenuAdd, afterInitFun=lambda obj: _AddToUiitems("NewTaskMenuItm", obj)),
        MenuTopoNode(label="Del Task", accelerator="Ctrl+D", fun=OnClickMenuDel, afterInitFun=lambda obj: _AddToUiitems("DelTaskMenuItm", obj)),
        MenuTopoNode(label="Rec Task", accelerator="Ctrl+R", fun=OnClickMenuRec, afterInitFun=lambda obj: _AddToUiitems("RecTaskMenuItm", obj)),
        MenuTopoSeparator(),
        MenuTopoNode(label="Move Task Up", accelerator="Ctrl+↑", fun=OnClickMenuUp, afterInitFun=lambda obj: _AddToUiitems("MoveUpMenuItm", obj)),
        MenuTopoNode(label="Move Task Down", accelerator="Ctrl+↓", fun=OnClickMenuDn, afterInitFun=lambda obj: _AddToUiitems("MoveDnMenuItm", obj)),
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
