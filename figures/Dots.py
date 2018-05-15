import numpy.random as rnd
import random
from matplotlib.patches import Circle
from figures.Figure import Figures


class DotsBuilder(Figures):
    @staticmethod
    def generate(xy, count=0):
        elements = []

        for i in range(count):
            xy = rnd.uniform(2.8, 7.2, 2)
            radius = rnd.uniform(0.01, 0.1)
            elements.append(Circle(xy=xy, radius=radius))

        return elements

    def generate_random(self, count=0):
        xy = rnd.uniform(2.8, 7.2, 2)

        if count == 0:
            count = random.randint(3, 10)

        return self.generate(xy, count=count)

