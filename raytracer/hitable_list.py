import math
from _ast import List

from raytracer.hitable import Hitable, HitRecord
from raytracer.ray import Ray


class HitableList(Hitable):
    def __init__(self, hitables=None):
        self.hitables = hitables

    def get_hitables(self):
        return self.hitables

    def hit(self,
            ray: Ray,
            t_min: float,
            t_max: float) -> HitRecord:
        hit_record = None
        closest_so_far = t_max
        for hitable in self.hitables:
            temp_record = hitable.hit(ray, t_min, closest_so_far)
            if temp_record is not None:
                closest_so_far = temp_record.get_t()
                hit_record = temp_record
        return hit_record
