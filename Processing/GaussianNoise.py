import numpy as np
from datetime import datetime
from Utilities import Logger


class GaussianNoise:
    def __init__(self):
        self.logs = Logger('log_' + datetime.strftime(datetime.now(), "%d_%m_%H_%M") + '.txt')

    def noise_image(self, image):
        row, col = image.shape
        self.logs.write_log("image = ", str(image))
        mean = 0
        sigma = 10
        gauss = np.random.normal(mean, sigma, (row, col))
        gauss = gauss.reshape(row, col)
        noisy = image + gauss
        return noisy
