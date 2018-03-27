import os
import cv2
from PIL import Image
from Processing.GaussianNoise import GaussianNoise


def process_image(output_image_path):
    image = cv2.imread("images/buffer/output.png", cv2.IMREAD_GRAYSCALE)  # реверснуть цвета?
    cv2.imwrite(
        "image/buffer/output.png",
        GaussianNoise().noise_image(image)
    )

    os.system('C:/Users/Дамир/PycharmProjects/figure-generator/outer_image_processing/GaussianBlur/bin/Debug'
              '/KernelConvolution.exe')
    os.system('C:/Users/Дамир/PycharmProjects/figure-generator/outer_image_processing/Sobel/bin/Debug'
              '/Sobel.exe')

    im = Image.open("C:/Directory/readyedges.png")
    black_point = (0, 0, 0, 255)
    if list(im.getdata()).count(black_point) == 729:
        im.close()
        return
    im.save(output_image_path)
    return im
