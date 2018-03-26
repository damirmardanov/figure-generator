from datetime import datetime
import cv2


class GaussianBlur:
    @staticmethod
    def filter_image(image_to_filter):
        start_time = datetime.now()

        # making image greyscale

        width = image_to_filter.width()
        height = image_to_filter.height()


