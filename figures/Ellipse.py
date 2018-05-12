import numpy.random as rnd
from matplotlib.patches import Ellipse
from figures.Figure import Figure


class EllipseBuilder(Figure):
    @staticmethod
    def generate(xy, width=0, height=0, angle=0):
        return Ellipse(xy=xy, width=width, height=height, angle=angle)

    def generate_random(self):
        width = rnd.uniform(1.0, 9.8)
        height = width * rnd.uniform(0.1, 0.8)
        xy = rnd.uniform(2.8, 7.2, 2)
        angle = rnd.rand() * 360
        return self.generate(xy, height, width, angle)
