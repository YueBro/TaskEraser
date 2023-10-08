from abc import ABCMeta, abstractmethod
from .act_event import ActEvnt


class ActSubscriber(metaclass=ABCMeta):
    @abstractmethod
    def OnEvnt(self, evnt: ActEvnt):
        raise NotImplemented("Need implementation")
