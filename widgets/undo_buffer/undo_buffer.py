from copy import deepcopy as dpcp


class UndoBuffer:
    def __init__(self, undoMaxNum=40):
        self.undoMaxNum = undoMaxNum
        self.undoBuffer = []
        self.redoBuffer = []

    def NewChange(self, changeInfo):
        if len(self.undoBuffer) >= self.undoMaxNum:
            self.undoBuffer.pop(0)
        self.undoBuffer.append(changeInfo)
        if len(self.redoBuffer) != 0:
            self.redoBuffer = []
    
    def Undo(self):
        return self._MoveEvntBtwnBuffersAndRetEvnt(self.undoBuffer, self.redoBuffer)

    def Redo(self):
        return self._MoveEvntBtwnBuffersAndRetEvnt(self.redoBuffer, self.undoBuffer)
    
    @staticmethod
    def _MoveEvntBtwnBuffersAndRetEvnt(fromBuffer: list, toBuffer: list):
        if len(fromBuffer) == 0:
            return None
        changeInfo = fromBuffer.pop(-1)
        toBuffer.append(changeInfo)
        return dpcp(changeInfo)
