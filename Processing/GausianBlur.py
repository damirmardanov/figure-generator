import cv2
import numpy as np


class GaussianBlur:
    @staticmethod
    def process(image_to_filter):
        return cv2.GaussianBlur(np.uint8(image_to_filter), (3, 3), 0, 0)
