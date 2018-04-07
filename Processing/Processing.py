import cv2
from Processing.GaussianNoise import GaussianNoise
from Processing.GausianBlur import GaussianBlur
from Processing.Canny import Canny


def process_image(output_image_path):
    image = cv2.imread("images/buffer/output.png", cv2.IMREAD_GRAYSCALE)

    noisy = GaussianNoise.process(image)
    clear = GaussianBlur.process(noisy)
    sobel_image = Canny.process(clear)

    black_point = (0, 0, 0, 255)
    if list(sobel_image).count(black_point) == 729:
        return
                                                        # записать это в отдельный метод ? (14-21)
    cv2.imwrite(
        output_image_path,
        sobel_image
    )

    return sobel_image
