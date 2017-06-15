from abc import ABC, abstractmethod, ABCMeta


class Hitable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def hit(self, ray, t_min,t_max, record):
        pass

class HitRecord:

    def __init__(self, t, p, normal):
        self.t = t
        self.p = p
        self.normal = normal
