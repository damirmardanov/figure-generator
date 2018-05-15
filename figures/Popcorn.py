import numpy.random as rnd
import random
from figures.Ellipse import EllipseBuilder
from figures.Figure import Figures


class PopcornBuilder(Figures):
    @staticmethod
    def generate(xy, count=0):
        elements = []

        for i in range(random.randint(3, 7)):
            width = rnd.uniform(1.0, 3.5)
            height = width * rnd.uniform(0.6, 1.0)
            x = rnd.uniform(xy[0] - 1.5, xy[0] + 1.5)
            y = rnd.uniform(xy[1] - 1.5, xy[1] + 1.5)
            angle = rnd.rand() * 360
            elements.append(EllipseBuilder.generate((x, y), width=width, height=height, angle=angle))

        return elements

    def generate_random(self, count=0):
        xy = rnd.uniform(2.8, 7.2, 2)

        if count == 0:
            count = random.randint(3, 7)

        return self.generate(xy, count=count)
