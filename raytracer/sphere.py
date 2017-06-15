from raytracer.hitable import Hitable

class Sphere(Hitable):

    def __init__(self, *args):
        self.center = args[0]
        self.radius = args[1]