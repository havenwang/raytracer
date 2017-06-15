import os

import math
import random

from raytracer.camera import Camera
from raytracer.hitable import Hitable
from raytracer.hitable_list import HitableList
from raytracer.ray import Ray
from raytracer.sphere import Sphere
from raytracer.vector import Vector


def color(ray: Ray, world: HitableList):
    hit_world = world.hit(ray, 0.0, float("inf"))
    if hit_world is not None:
        normal = hit_world.get_normal()
        return 0.5 * Vector(normal.values[0] + 1, normal.values[1] + 1, normal.values[2] + 1)
    else:
        unit_direction = r.direction().normalize()
        t = 0.5 * (unit_direction.values[1] + 1)
        return (1.0 - t) * Vector(1., 1., 1.) + t * Vector(0.5, 0.7, 1.0)


image_file = os.path.join(os.getcwd(), 'image.txt')
with open(image_file, 'w') as f:
    nx = 200
    ny = 100
    ns = 100
    f.write("P3\n{} {}\n255\n".format(nx, ny))
    lower_left_corner = Vector(-2.0, -1.0, -1.0)
    horizontal = Vector(4.0, 0.0, 0.0)
    vertical = Vector(0.0, 2.0, 0.0)
    origin = Vector(0.0, 0.0, 0.0)
    spheres = [Sphere(Vector(0, 0, -1), 0.5), Sphere(Vector(0, -100.5, -1), 100)]
    camera = Camera()
    for j in range(ny - 1, -1, -1):
        for i in range(0, nx):
            u = float(i) / nx
            v = float(j) / ny

            col = Vector(0, 0, 0)
            for s in range(0, ns):
                u = (i + random.random()) / nx
                v = (j + random.random()) / ny
                r = camera.get_ray(u, v)
                p = r.point_at_parameter(2.0)
                col += color(r, HitableList(spheres))
            col.div_by_value(ns)

            ir = (int(255.99 * col.values[0]))
            ig = (int(255.99 * col.values[1]))
            ib = (int(255.99 * col.values[2]))
            f.write("{} {} {}\n".format(ir, ig, ib))
