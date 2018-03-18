import numpy.random as rnd
from matplotlib.patches import Ellipse


class CircleBuilder:
    @staticmethod
    def generate_random():
        width = rnd.uniform(1.0, 9.8)
        height = width * rnd.uniform(0.8, 1.0)
        return Ellipse(xy=rnd.uniform(2.8, 7.2, 2), width=width, height=height, angle=rnd.rand() * 360)
