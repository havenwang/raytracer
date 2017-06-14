import os

from raytracer.ray import Ray
from raytracer.vector import Vector


def hit_sphere(center, radius, r):
    A = r.origin()
    B = r.direction()
    C = center

    a = B.inner(B)
    b = 2.0 * B.inner(A - C)
    c = (A - C).inner(A - C) - radius ** 2
    discriminant = b ** 2 - 4 * a * c
    return (discriminant >= 0)


def color(r):
    if (hit_sphere(Vector(0, 0, -1), 0.5, r)):
        return Vector(1, 0, 0)
    unit_direction = r.direction().normalize()
    t = 0.5 * (unit_direction.values[1] + 1)
    return (1.0 - t) * Vector(1., 1., 1.) + t * Vector(0.5, 0.7, 1.0)


image_file = os.path.join(os.getcwd(), 'image.txt')
with open(image_file, 'w') as f:
    nx = 200
    ny = 100
    f.write("P3\n{} {}\n255\n".format(nx, ny))
    lower_left_corner = Vector(-2.0, -1.0, -1.0)
    horizontal = Vector(4.0, 0.0, 0.0)
    vertical = Vector(0.0, 2.0, 0.0)
    origin = Vector(0.0, 0.0, 0.0)
    for j in range(ny - 1, -1, -1):
        for i in range(0, nx):
            u = float(i) / nx
            v = float(j) / ny
            r = Ray(origin, lower_left_corner + u * horizontal + v * vertical)
            col = color(r)
            ir = (int(255.99 * col.values[0]))
            ig = (int(255.99 * col.values[1]))
            ib = (int(255.99 * col.values[2]))
            f.write("{} {} {}\n".format(ir, ig, ib))
