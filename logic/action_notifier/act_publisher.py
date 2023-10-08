from .act_consts import *
from .act_event import ActEvnt
from .act_subscriber import ActSubscriber

from typing import Union, List


class _PseudoActSubscriber(ActSubscriber):
    def __init__(self, fun: function) -> None:
        super().__init__()
        assert isinstance(fun, function)
        self.fun = fun

    def OnEvnt(self, evnt: ActEvnt):
        self.fun(evnt)


class ActPublisher:
    lastAction = ACT_STATE_INIT
    subscribers: List[ActSubscriber] = []

    @classmethod
    def Register(cls, subscriber: Union[function, ActSubscriber]):
        if isinstance(subscriber, ActSubscriber):
            ActSubscriber.append(subscriber)
        elif isinstance(subscriber, function):
            ActSubscriber.append(_PseudoActSubscriber(subscriber))
        else:
            raise Exception("Invalid subscriber type")

    @classmethod
    def Publish(cls, evntContent: ActEvnt):
        assert isinstance(evntContent, ActEvnt)
        evntContent.fromAction = cls.lastAction
        cls.lastAction = evntContent.toAction
        for subscriber in cls.subscribers:
            subscriber.OnEvnt(evntContent)
