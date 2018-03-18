import numpy.random as rnd
import random
from matplotlib.patches import Circle


class DotsBuilder:
    @staticmethod
    def generate_random(count=0):
        elements = []
        if count == 0:
            for i in range(random.randint(3, 10)):
                elements.append(Circle(xy=rnd.uniform(2.8, 7.2, 2), radius=rnd.uniform(0.01, 0.1)))
        else:
            for i in range(count):
                elements.append(Circle(xy=rnd.uniform(2.8, 7.2, 2), radius=rnd.uniform(0.01, 0.1)))
        return elements
