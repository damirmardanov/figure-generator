import numpy.random as rnd

from matplotlib.patches import Rectangle


class BarBuilder:
    @staticmethod
    def generate_random():
        return Rectangle(xy=rnd.uniform(2.8, 7.2, 2), width=rnd.uniform(1.0, 9.8), height=rnd.uniform(1.0, 9.8),
                         angle=rnd.rand() * 360)
