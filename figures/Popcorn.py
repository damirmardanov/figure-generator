import numpy.random as rnd
import random
from matplotlib.patches import Ellipse


class PopcornBuilder:
    @staticmethod
    def generate_random():
        elements = []
        center = rnd.uniform(2.8, 7.2, 2)
        for j in range(random.randint(3, 7)):
            width = rnd.uniform(1.0, 3.5)
            height = width * rnd.uniform(0.6, 1.0)
            x = rnd.uniform(center[0] - 1.5, center[0] + 1.5)
            y = rnd.uniform(center[1] - 1.5, center[1] + 1.5)
            elements.append(Ellipse(xy=(x, y), width=width, height=height, angle=rnd.rand() * 360))
        return elements
