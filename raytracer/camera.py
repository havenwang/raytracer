import math
from vector import Vector

from raytracer.ray import Ray


class Camera:
    def __init__(self,
                 lower_left_corner=Vector(-2, -1, -1),
                 horizontal=Vector(4, 0, 0),
                 vertical=Vector(0, 2, 0),
                 origin=Vector(0, 0, 0)):
        self.lower_left_corner = lower_left_corner
        self.horizontal = horizontal
        self.vertical = vertical
        self.origin = origin

    def origin(self):
        return self.origin

    def get_ray(self, u: float, v: float):
        return Ray(self.origin, self.lower_left_corner + u * self.horizontal + v * self.vertical - self.origin)
