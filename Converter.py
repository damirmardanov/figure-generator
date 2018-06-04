
class Converter:
    @staticmethod
    def convert_image_to_csv_row(image, figure_type):
        row_final = []
        if figure_type == "Bar":
            row_final.append('1')
        elif figure_type == "Circle":
            row_final.append('2')
        elif figure_type == "Dots":
            row_final.append('3')
        elif figure_type == "Ellipse":
            row_final.append('4')
        elif figure_type == "Popcorn":
            row_final.append('5')
        else:
            row_final.append('0')
        try:
            for pixel in list(image):
                if pixel[0] != 0 or pixel[1] != 0 or pixel[2] != 0:
                    row_final.append(str('1'))
                else:
                    row_final.append(str('0'))
        except:
            pass

        return row_final
