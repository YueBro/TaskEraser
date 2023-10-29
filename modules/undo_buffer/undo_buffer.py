from copy import deepcopy as dpcp


class UndoBuffer:
    def __init__(self, currState=None, undoMaxNum=40):
        self.undoMaxNum = undoMaxNum
        self.stateBuffer = None
        self.idx = None
        self.initialize(currState)

    def append_change(self, changeInfo):
        self.stateBuffer = self.stateBuffer[:self.idx+1] + [changeInfo] # new change
        self.stateBuffer = self.stateBuffer[-self.undoMaxNum:]          # truncate size
        self.idx = len(self.stateBuffer) - 1
    
    def undo(self):
        if self.idx >= 1:
            self.idx -= 1
            return dpcp(self.stateBuffer[self.idx])
        return None

    def redo(self):
        if self.idx < len(self.stateBuffer)-1:
            self.idx += 1
            return dpcp(self.stateBuffer[self.idx])
        return None

    def initialize(self, state):
        self.stateBuffer = [state]
        self.idx = 0
