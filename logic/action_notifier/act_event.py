from .act_consts import *


class ActEvnt:
    def __init__(self, act, data = None) -> None:
        assert isinstance(act, int)
        self.fromAction = ACT_EVNT_INIT
        self.toAction = act
        self.data = data
