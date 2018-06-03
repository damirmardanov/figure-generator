import matplotlib.pyplot as plt
import numpy.random as rnd


class Plotter:
    @staticmethod
    def plot(figure=None, figures=None, filename='output.png', height=27, width=27):
        fig = plt.figure(0, figsize=(height / 102, width / 102), dpi=102)
        ax = fig.add_subplot(111, aspect='equal')
        if (figure is not None) and (figures is None):
            ax.add_artist(figure)
        else:
            for figure in figures:
                ax.add_artist(figure)
                figure.set_clip_box(ax.bbox)
                figure.set_alpha(rnd.rand())
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        plt.axis('off')
        plt.savefig(filename)
        plt.clf()

