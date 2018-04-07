import cv2


class Sobel:
    @staticmethod
    def process(image, kernel_size=5):
        return cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=kernel_size)
