import numpy as np
from datetime import datetime
from Utilities import Logger


class GaussianNoise:
    def __init__(self):
        self.logs = Logger('log_' + datetime.strftime(datetime.now(), "%d_%m_%H_%M") + '.txt')

    @staticmethod
    def process(image):
        row, col = image.shape
        mean = -35
        sigma = 10
        gauss = np.random.normal(mean, sigma, (row, col))
        for i in range(0, row):
            for j in range(0, col):
                if gauss[i][j] > 0:
                    gauss[i][j] = 0
        gauss = gauss.reshape(row, col)
        noisy = image + gauss
        return np.round(noisy).astype(int)
