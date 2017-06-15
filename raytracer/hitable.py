from abc import ABC, abstractmethod, ABCMeta


class HitRecord:
    def __init__(self, t=None, p=None, normal=None):
        self.t = t
        self.p = p
        self.normal = normal

    def get_normal(self):
        return self.normal

    def get_p(self):
        return self.p

    def get_t(self):
        return self.t


class Hitable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def hit(self, ray, t_min, t_max) -> HitRecord:
        pass
