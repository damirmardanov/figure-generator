from __future__ import division
from datetime import datetime
from Utilities import Cleaner, Writer, Logger
from Plotter import Plotter
from Processing import Processing
from Converter import Converter
from figures.Bar import BarBuilder
from figures.Circle import CircleBuilder
from figures.Dots import DotsBuilder
from figures.Ellipse import EllipseBuilder
from figures.Popcorn import PopcornBuilder
from tkinter import *


def process():
    # global root
    logs = Logger('log_' + datetime.strftime(datetime.now(), "%d_%m_%H_%M") + '.txt')
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

        bar = BarBuilder().generate_random()
        Plotter.plot(bar, filename='images/buffer/output.png')
        image = Processing.process_image('images/Bars/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Bar")
        )

        iterations += 1
    print("Bars created")

    iterations = 1
    for i in range(0, figure_numbers.get("Circle")):
        print("Circle: step " + str(iterations) + " of " + str(figure_numbers.get("Circle")))

        circle = CircleBuilder().generate_random()
        Plotter.plot(circle, filename='images/buffer/output.png')
        image = Processing.process_image('images/Circles/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Circle")
        )

        iterations += 1
    print("Circles created")

    iterations = 1
    for i in range(0, figure_numbers.get("Dots")):
        print("Dots: step " + str(iterations) + " of " + str(figure_numbers.get("Dots")))

        dots = DotsBuilder().generate_random()
        Plotter.plot(figures=dots, filename='images/buffer/output.png')
        image = Processing.process_image('images/Dots/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Dots")
        )

        iterations += 1
    print("Dots created")

    iterations = 1
    for i in range(0, figure_numbers.get("Ellipse")):
        print("Ellipse: step " + str(iterations) + " of " + str(figure_numbers.get("Ellipse")))

        ellipse = EllipseBuilder().generate_random()
        Plotter.plot(ellipse, filename='images/buffer/output.png')
        image = Processing.process_image('images/Ellipses/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Ellipse")
        )

        iterations += 1
    print("Ellipse created")

    iterations = 1
    for i in range(0, figure_numbers.get("Popcorn")):
        print("Popcorn: step " + str(iterations) + " of " + str(figure_numbers.get("Popcorn")))

        popcorn = PopcornBuilder().generate_random()
        Plotter.plot(figures=popcorn, filename='images/buffer/output.png')
        image = Processing.process_image('images/Popcorn/sample' + str(iterations) + '.png')

        writer.write_row_to_file(
            Converter.convert_image_to_csv_row(image, "Popcorn")
        )

        iterations += 1
    print("Popcorn created")

    return


class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        input_paddingy = 3
        label_paddingx = 5
        input_paddingx = 5
        self.bar_count = StringVar()
        self.circle_count = StringVar()
        self.ellipse_count = StringVar()
        self.popcorn_count = StringVar()
        self.dots_count = StringVar()
        self.res_h = StringVar()
        self.res_w = StringVar()
        self.file = StringVar()
        self._root().title("Генератор обучающей выборки")
        self.bar_input = Entry(self, textvariable=self.bar_count)
        self.circle_input = Entry(self, textvariable=self.circle_count)
        self.dots_input = Entry(self, textvariable=self.ellipse_count)
        self.ellipse_input = Entry(self, textvariable=self.popcorn_count)
        self.popcorn_input = Entry(self, textvariable=self.dots_count)
        self.resolution_h_input = Entry(self, textvariable=self.res_h)
        self.resolution_w_input = Entry(self, textvariable=self.res_w)
        self.file_input = Entry(self, textvariable=self.file)

        self.bar_count.set("0")
        self.circle_count.set("0")
        self.dots_count.set("0")
        self.ellipse_count.set("0")
        self.popcorn_count.set("0")
        self.res_h.set("27")
        self.res_w.set("27")
        self.file.set("training.csv")

        menubar=Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Выход", command=self.destroy)

        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="Помощь", command=self.destroy)
        aboutmenu.add_command(label="О программе", command=self.destroy)

        menubar.add_cascade(label="Файл", menu=filemenu)
        menubar.add_cascade(label="О программе", menu=aboutmenu)
        self.config(menu=menubar)

        self.start_button = Button(self,
                                   text="Начать генерацию",
                                   width=20, height=2,
                                   bg="white", fg="black", command=process)

        Label(self, text='Количество генерируемых объектов округлой формы":')\
            .grid(row=0, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.circle_input.grid(row=0, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Количество генерируемых объектов овальной формы:')\
            .grid(row=1, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.ellipse_input.grid(row=1, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Количество генерируемых объектов "Стержень":')\
            .grid(row=2, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.bar_input.grid(row=2, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Количество генерируемых объектов "Попкорн":')\
            .grid(row=3, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.popcorn_input.grid(row=3, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Количество генерируемых объектов "Скопление точек":')\
            .grid(row=4, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.dots_input.grid(row=4, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Высота генерируемых изображений:')\
            .grid(row=5, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.resolution_h_input.grid(row=5, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Ширина генерируемых изображений:')\
            .grid(row=6, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.resolution_w_input.grid(row=6, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Сохранить в:')\
            .grid(row=7, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.file_input.grid(row=7, column=1, padx=input_paddingx, sticky="w")

        self.start_button.grid(row=8, columnspan=2, pady=input_paddingy)

    def on_button(self):
        print(self.bar_input.get())


app = Application()
app.mainloop()
