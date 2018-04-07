import cv2
from Processing.GaussianNoise import GaussianNoise
from Processing.GausianBlur import GaussianBlur


def process_image(output_image_path):
    image = cv2.imread("images/buffer/output.png", cv2.IMREAD_GRAYSCALE)
    noisy = GaussianNoise.process(image)
    cv2.imwrite(
        'images/buffer/noisy.png',
        noisy
    )
    clear = GaussianBlur.process(noisy)
    cv2.imwrite(
        'images/buffer/clear.png',
        clear
    )
    sobel_image = cv2.Canny(clear, 1, 120)  # Sobel.process(clear)

    black_point = (0, 0, 0, 255)
    if list(sobel_image).count(black_point) == 729:
        return

    cv2.imwrite(
        output_image_path,
        sobel_image
    )

    return sobel_image
