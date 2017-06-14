import math
from vector import Vector


class Ray:

    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2) """
        if len(args) == 0:
            self.A = None
            self.B = None
        else:
            self.A = args[0]
            self.B = args[1]

    def origin(self):
        return self.A

    def direction(self):
        return self.B

    def point_at_parameter(self, t):
        return self.A + t * self.B
