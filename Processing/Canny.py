import cv2


class Canny:
    @staticmethod
    def process(image):
        return cv2.Canny(image, 1, 100)
