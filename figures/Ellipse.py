import numpy.random as rnd
from matplotlib.patches import Ellipse


class EllipseBuilder:
    def init(self):
        return

    def generate_random(self):
        width = rnd.uniform(1.0, 9.8)
        height = width * rnd.uniform(0.1, 0.8)

        e = Ellipse(xy=rnd.uniform(2.8, 7.2, 2), width=width, height=height, angle=rnd.rand() * 360)
