from abc import ABC, abstractmethod


class Hitable:
    __metaclass__ = ABCMeta


    @abstractmethod
    def hit(self, ray, t_min,t_max, record):
        pass