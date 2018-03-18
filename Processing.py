import os
from PIL import Image


class Processing:
    @staticmethod
    def process_image(output_image_path):
        os.system('C:/Users/Дамир/Desktop/Учеба/Диплом/Project/GaussianBlur/bin/Debug/KernelConvolution.exe')
        os.system('C:/Users/Дамир/Desktop/Учеба/Диплом/Project/Sobel/bin/Debug/Sobel.exe')

        im = Image.open("C:/Directory/readyedges.png")
        black_point = (0, 0, 0, 255)
        if list(im.getdata()).count(black_point) == 729:
            im.close()
            return
        im.save(output_image_path)
        im.close()
