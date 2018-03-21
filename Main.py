from __future__ import division
from Utilities import Cleaner, Writer
from Plotter import Plotter
from Processing import Processing
from Converter import Converter
from figures.Bar import BarBuilder
from figures.Circle import CircleBuilder
from figures.Dots import DotsBuilder
from figures.Ellipse import EllipseBuilder
from figures.Popcorn import PopcornBuilder


def main():
    writer = Writer(input("Input csv file name: "))
    figure_numbers = {}
    figure_numbers.update({"Bar": int(input("Input number of 'Bar' pictures: "))})
    figure_numbers.update({"Circle": int(input("Input number of 'Circle' pictures: "))})
    figure_numbers.update({"Dots": int(input("Input number of 'Dots' pictures: "))})
    figure_numbers.update({"Ellipse": int(input("Input number of 'Ellipse' pictures: "))})
    figure_numbers.update({"Popcorn": int(input("Input number of 'Popcorn' pictures: "))})

    Cleaner().clear_output_images()

    iterations = 1
    for i in range(0, figure_numbers.get("Bar")):
        print("Bar: step " + str(iterations) + " of " + str(figure_numbers.get("Bar")))

        bar = BarBuilder.generate_random()
        Plotter.plot(bar, filename='C:/Directory/output.png')
        image = Processing.process_image('images/Bars/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Bar")
        )

        iterations += 1
    print("Bars created")

    iterations = 1
    for i in range(0, figure_numbers.get("Circle")):
        print("Circle: step " + str(iterations) + " of " + str(figure_numbers.get("Circle")))

        circle = CircleBuilder.generate_random()
        Plotter.plot(circle, filename='C:/Directory/output.png')
        image = Processing.process_image('images/Circles/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Circle")
        )

        iterations += 1
    print("Circles created")

    iterations = 1
    for i in range(0, figure_numbers.get("Dots")):
        print("Dots: step " + str(iterations) + " of " + str(figure_numbers.get("Dots")))

        dots = DotsBuilder.generate_random()
        Plotter.plot(figures=dots, filename='C:/Directory/output.png')
        image = Processing.process_image('images/Dots/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Dots")
        )

        iterations += 1
    print("Dots created")

    iterations = 1
    for i in range(0, figure_numbers.get("Ellipse")):
        print("Ellipse: step " + str(iterations) + " of " + str(figure_numbers.get("Ellipse")))

        ellipse = EllipseBuilder.generate_random()
        Plotter.plot(ellipse, filename='C:/Directory/output.png')
        image = Processing.process_image('images/Ellipses/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Ellipse")
        )

        iterations += 1
    print("Ellipse created")

    iterations = 1
    for i in range(0, figure_numbers.get("Popcorn")):
        print("Popcorn: step " + str(iterations) + " of " + str(figure_numbers.get("Popcorn")))

        popcorn = PopcornBuilder.generate_random()
        Plotter.plot(figures=popcorn, filename='C:/Directory/output.png')
        image = Processing.process_image('images/Popcorn/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Popcorn")
        )

        iterations += 1
    print("Popcorn created")

    return


if __name__ == "__main__":
    main()
