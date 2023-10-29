from __future__ import annotations  # so that "class X : fun(self) -> X" can be realized

import tkinter as tk
from inspect import isfunction

from typing import List


class MenuTopoNode:
    def __init__(self, label: str = None, accelerator: str = None, subNodes: list = None, fun = ...) -> None:
        if label is None:
            assert subNodes is not None
        if subNodes is None:
            subNodes = []
        else:
            assert fun is ..., f"{label=}, {accelerator=}, {fun=}"
            assert accelerator is None
        assert all([isinstance(node, MenuTopoNode) or isinstance(node, MenuTopoSeparator) for node in subNodes])
        assert fun is ... or isfunction(fun)
        self.label: str = label
        self.subNodes: List[MenuTopoNode] = subNodes
        self.accelerator = accelerator
        self.fun = fun
        self.menuWidgt: tk.Menu = None      # tk.Menu is stored here (after calling SetupMenu()), for changing menu states
    
    def HasSubs(self) -> bool:
        return len(self.subNodes) > 0
    
    def IsRoot(self) -> bool:
        return self.label is None

    def __getitem__(self, other: str) -> MenuTopoNode:
        assert isinstance(other, str)
        for node in self.subNodes:
            if node.label == other:
                return node
        return None
    
    def __str__(self):
        return f"label={self.label} accelerator={self.accelerator}"


class MenuTopoSeparator:
    pass
