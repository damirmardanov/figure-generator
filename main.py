from __future__ import division
import matplotlib.pyplot as plt
import numpy.random as rnd
import random
from matplotlib.patches import Ellipse
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
from PIL import Image
import os
from figures.Bar import BarBuilder
from figures.Circle import CircleBuilder
from figures.Dots import DotsBuilder
from figures.Ellipse import EllipseBuilder
from figures.Popcorn import PopcornBuilder

folder = 'C:/Users/Дамир/Desktop/Учеба/Диплом/training_images'
# print('clearing...')
# for the_file in os.listdir(folder):
#    file_path = os.path.join(folder, the_file)
#    try:
#        if os.path.isfile(file_path):
#            os.unlink(file_path)
#    except Exception as e:
#        print(e)

NUM = 20
iterations = 1
for i in range(1, NUM):
    if i < 4000:
        e = EllipseBuilder.generate_random()
    elif 4000 <= i < 8000:
        e = BarBuilder.generate_random()
    elif 8000 <= i < 12000:
        elements = DotsBuilder.generate_random()
    elif 12000 <= i < 16000:
        e = CircleBuilder.generate_random()
    elif 16000 <= i < 20000:
        elements = PopcornBuilder.generate_random()
    fig = plt.figure(0, figsize=(27 / 102, 27 / 102), dpi=102)
    ax = fig.add_subplot(111, aspect='equal')
    for e in elements:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(rnd.rand())
    # try:
    #     e.set_facecolor(rnd.rand(3))
    # except Exception as exc:
    #     e.set_color(rnd.rand(3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    plt.axis('off')
    plt.savefig('output.png')

    print('step ' + str(iterations) + ' of ' + str(NUM))
    os.system('MOVE /Y output.png C:/Directory/output.png')
    os.system('C:/Users/Дамир/Desktop/Учеба/Диплом/Project/GaussianBlur/bin/Debug/KernelConvolution.exe')
    os.system('C:/Users/Дамир/Desktop/Учеба/Диплом/Project/Sobel/bin/Debug/Sobel.exe')

    im = Image.open("C:/Directory/readyedges.png")
    list_of_binary_edge = list()
    black_point = (0, 0, 0, 255);
    white_pixel = (255, 255, 255);
    black_pixel = (0, 0, 0);
    if list(im.getdata()).count(black_point) == 729:
        im.close()
        continue
    im.save('training_images/white_sample' + str(iterations) + '.png')
    im.close()

    plt.clf()
    iterations += 1
