from .act_consts import *
from .act_event import ActEvnt
from .act_subscriber import ActSubscriber

from typing import Union, Any, List, Dict

from inspect import isfunction


class _PseudoActSubscriber(ActSubscriber):
    def __init__(self, fun, fun_end=None) -> None:
        super().__init__()
        assert isfunction(fun)
        self.fun = fun
        self.fun_end = fun_end

    def OnEvnt(self, evnt: ActEvnt):
        self.fun(evnt)
    
    def OnEvntEnd(self, evnt: ActEvnt):
        if self.fun_end is not None:
            self.fun_end(evnt)


class ActPublisher:
    lastAction = ACT_EVNT_INIT
    toEvntOnlySubscribers: Dict[int, List[ActSubscriber]] = {}
    AnySubscribers: List[ActSubscriber] = []

    @classmethod
    def RegisterTheToEvntOnly(cls, evnt, subscriber: Union[Any, ActSubscriber]):
        if isinstance(subscriber, ActSubscriber):
            s = subscriber
        elif isfunction(subscriber):
            s = _PseudoActSubscriber(subscriber)
        else:
            raise Exception("Invalid subscriber type")
        cls.toEvntOnlySubscribers[evnt] = cls.toEvntOnlySubscribers.get(evnt, []) + [s]

    @classmethod
    def RegisterAnyEvnt(cls, subscriber: Union[Any, ActSubscriber]):
        print(subscriber, type(subscriber))
        if isinstance(subscriber, ActSubscriber):
            cls.AnySubscribers.append(subscriber)
        elif isfunction(subscriber):
            cls.AnySubscribers.append(_PseudoActSubscriber(subscriber))
        else:
            raise Exception("Invalid subscriber type")

    @classmethod
    def Publish(cls, evntContent: ActEvnt):
        assert isinstance(evntContent, ActEvnt)
        evntContent.fromAction = cls.lastAction
        cls.lastAction = evntContent.toAction
        
        for subscriber in cls.toEvntOnlySubscribers.get(evntContent.fromAction, []):
            subscriber.OnEvntEnd(evntContent)
        for subscriber in cls.AnySubscribers:
            subscriber.OnEvntEnd(evntContent)

        for subscriber in cls.toEvntOnlySubscribers.get(evntContent.toAction, []):
            subscriber.OnEvnt(evntContent)
        for subscriber in cls.AnySubscribers:
            subscriber.OnEvnt(evntContent)
