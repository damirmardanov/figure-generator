import os
from PIL import Image


class Processing:
    @staticmethod
    def process_image(output_image_path):
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
