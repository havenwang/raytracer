import math

from raytracer.hitable import Hitable, HitRecord
from raytracer.ray import Ray


class Sphere(Hitable):
    def __init__(self, *args):
        self.center = args[0]
        self.radius = args[1]

    def hit(self,
            ray: Ray,
            t_min: float,
            t_max: float) -> HitRecord:
        distance_to_center = ray.origin() - self.center
        a = ray.direction().inner(ray.direction())
        b = distance_to_center.inner(ray.direction())
        c = distance_to_center.inner(distance_to_center)
        discriminant = b * b - a * c
        if discriminant > 0:
            t = (-b - math.sqrt(discriminant)) / a
            if t_max > t > t_min:
                return self.calculate_normal(t, ray)

            t = (-b + math.sqrt(discriminant)) / a
            if t_max > t > t_min:
                return self.calculate_normal(t, ray)
        else:
            return None

    def calculate_normal(self,
                         t: float,
                         ray: Ray) -> HitRecord:
        record = HitRecord()
        record.t = t
        record.p = ray.point_at_parameter(record.t)
        record.normal = (record.p - self.center) / self.radius
        return record
