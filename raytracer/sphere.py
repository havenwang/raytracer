import math

from raytracer.hitable import Hitable
from raytracer.ray import Ray


class Sphere(Hitable):
    def __init__(self, *args):
        self.center = args[0]
        self.radius = args[1]

    def hit(self,
            ray: Ray,
            t_min: float,
            t_max: float,
            record):
        distance_to_center = ray.origin() - self.center
        a = ray.direction().inner(ray.direction())
        b = distance_to_center.inner(ray.direction())
        c = distance_to_center.inner(distance_to_center)
        discriminant = b * b - a * c
        if discriminant > 0:
            temp = (-b - math.sqrt(discriminant)) / a
            if t_max > temp > t_min:
                # TODO: Need to implement hit record class first
                pass

            temp = (-b + math.sqrt(discriminant)) / a
            if t_max > temp > t_min:
                # TODO: Need to implement hit record class first
                pass
        return False
