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
from tkinter import ttk


class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        validate_count = (self.register(self.on_validate_count),
                          '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validate_res = (self.register(self.on_validate_res),
                        '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
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
        self.bar_input = Entry(self, textvariable=self.bar_count,
                               validate="key", validatecommand=validate_count)
        self.circle_input = Entry(self, textvariable=self.circle_count,
                                  validate="key", validatecommand=validate_count)
        self.dots_input = Entry(self, textvariable=self.ellipse_count,
                                validate="key", validatecommand=validate_count)
        self.ellipse_input = Entry(self, textvariable=self.popcorn_count,
                                   validate="key", validatecommand=validate_count)
        self.popcorn_input = Entry(self, textvariable=self.dots_count,
                                   validate="key", validatecommand=validate_count)
        self.resolution_h_input = Entry(self, textvariable=self.res_h,
                                        validate="key", validatecommand=validate_res)
        self.resolution_w_input = Entry(self, textvariable=self.res_w,
                                        validate="key", validatecommand=validate_res)
        self.file_input = Entry(self, textvariable=self.file)

        self.bar_count.set("0")
        self.circle_count.set("0")
        self.dots_count.set("0")
        self.ellipse_count.set("0")
        self.popcorn_count.set("0")
        self.res_h.set("27")
        self.res_w.set("27")
        self.file.set("training.csv")

        menubar = Menu(self)
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
                                   bg="white", fg="black", command=self.process)

        Label(self, text='Количество генерируемых объектов округлой формы:') \
            .grid(row=0, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.circle_input.grid(row=0, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Количество генерируемых объектов овальной формы:') \
            .grid(row=1, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.ellipse_input.grid(row=1, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Количество генерируемых объектов "Стержень":') \
            .grid(row=2, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.bar_input.grid(row=2, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Количество генерируемых объектов "Попкорн":') \
            .grid(row=3, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.popcorn_input.grid(row=3, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Количество генерируемых объектов "Скопление точек":') \
            .grid(row=4, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.dots_input.grid(row=4, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Высота генерируемых изображений:') \
            .grid(row=5, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.resolution_h_input.grid(row=5, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Ширина генерируемых изображений:') \
            .grid(row=6, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.resolution_w_input.grid(row=6, column=1, padx=input_paddingx, sticky="w")

        Label(self, text='Сохранить в:') \
            .grid(row=7, column=0, padx=label_paddingx, pady=input_paddingy, sticky="e")
        self.file_input.grid(row=7, column=1, padx=input_paddingx, sticky="w")

        self.start_button.grid(row=8, columnspan=2, pady=input_paddingy)

    def on_validate_count(self, d='', i='', P='', s='', S='', v='', V='', W=''):
        try:
            if P == '':
                return False
            if int(P) == 0:
                return True
            else:
                return 0 <= int(P) <= 100000
        except ValueError:
            return False

    def on_validate_res(self, d='', i='', P='', s='', S='', v='', V='', W=''):
        try:
            if P == '':
                return False
            if int(P) == 0:
                return True
            else:
                return 0 < int(P) <= 2000
        except ValueError:
            return False

    def process(self):
        logs = Logger('log_' + datetime.strftime(datetime.now(), "%d_%m_%H_%M") + '.txt')
        figure_numbers = {
            "Bar": int(self.bar_count.get()),
            "Circle": int(self.circle_count.get()),
            "Ellipse": int(self.ellipse_count.get()),
            "Dots": int(self.dots_count.get()),
            "Popcorn": int(self.popcorn_count.get())
        }
        writer = Writer(self.file.get())
        Cleaner().clear_output_images()

        iterations = 1
        for i in range(0, figure_numbers.get("Bar")):
            print("Bar: step " + str(iterations) + " of " + str(figure_numbers.get("Bar")))

            bar = BarBuilder().generate_random()
            Plotter.plot(bar, filename='images/buffer/output.png',
                         height=int(self.res_h.get()), width=int(self.res_w.get()))
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
            Plotter.plot(circle, filename='images/buffer/output.png',
                         height=int(self.res_h.get()), width=int(self.res_w.get()))
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
            Plotter.plot(figures=dots, filename='images/buffer/output.png',
                         height=int(self.res_h.get()), width=int(self.res_w.get()))
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
            Plotter.plot(ellipse, filename='images/buffer/output.png',
                         height=int(self.res_h.get()), width=int(self.res_w.get()))
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
            Plotter.plot(figures=popcorn, filename='images/buffer/output.png',
                         height=int(self.res_h.get()), width=int(self.res_w.get()))
            image = Processing.process_image('images/Popcorn/sample' + str(iterations) + '.png')

            writer.write_row_to_file(
                Converter.convert_image_to_csv_row(image, "Popcorn")
            )

            iterations += 1
        print("Popcorn created")

        return


class ProgressWindow(Tk):
    def __init__(self, circle_count=0, ellipse_count=0, bar_count=0, dots_count=0, popcorn_count=0):
        Tk.__init__(self)
        input_paddingy = 1
        label_paddingx = 5
        label_paddingy = 1

        self.current_circle_count = circle_count
        self.current_ellipse_count = ellipse_count
        self.current_bar_count = bar_count
        self.current_dots_count = 23115
        self.current_popcorn_count = 0

        self._root().title("Генератор обучающей выборки")

        self.pb_bar = ttk.Progressbar(self, orient="horizontal",
                                      length=350, mode="determinate")

        self.pb_circle = ttk.Progressbar(self, orient="horizontal",
                                         length=350, mode="determinate")

        self.pb_ellipse = ttk.Progressbar(self, orient="horizontal",
                                          length=350, mode="determinate")

        self.pb_dots = ttk.Progressbar(self, orient="horizontal",
                                       length=350, mode="determinate")

        self.pb_popcorn = ttk.Progressbar(self, orient="horizontal",
                                          length=350, mode="determinate")

        Label(self,
              text='Объекты округлой формы: ' + str(self.current_circle_count) + " из " + str(circle_count)) \
            .grid(row=0, column=0, padx=label_paddingx, pady=label_paddingy, sticky="w")
        self.pb_circle \
            .grid(row=1, column=0, padx=label_paddingx, pady=input_paddingy, sticky="w")

        Label(self,
              text='Объекты овальной формы: ' + str(self.current_ellipse_count) + " из " + str(ellipse_count)) \
            .grid(row=2, column=0, padx=label_paddingx, pady=label_paddingy, sticky="w")
        self.pb_ellipse \
            .grid(row=3, column=0, padx=label_paddingx, pady=input_paddingy, sticky="w")

        Label(self,
              text='Объекты типа "Стержень": ' + str(self.current_bar_count) + " из " + str(bar_count)) \
            .grid(row=4, column=0, padx=label_paddingx, pady=label_paddingy, sticky="w")
        self.pb_bar \
            .grid(row=5, column=0, padx=label_paddingx, pady=input_paddingy, sticky="w")

        Label(self,
              text='Объекты типа "Скопление точек": ' + str(self.current_dots_count) + " из " + str(dots_count)) \
            .grid(row=6, column=0, padx=label_paddingx, pady=label_paddingy, sticky="w")
        self.pb_dots \
            .grid(row=7, column=0, padx=label_paddingx, pady=input_paddingy, sticky="w")

        Label(self,
              text='Объекты типа "Попкорн": ' + str(self.current_popcorn_count) + " из " + str(popcorn_count)) \
            .grid(row=8, column=0, padx=label_paddingx, pady=label_paddingy, sticky="w")
        self.pb_popcorn \
            .grid(row=9, column=0, padx=label_paddingx, pady=5, sticky="w")

        self.end_button = Button(self,
                                 text="Завершить",
                                 width=20, height=2,
                                 bg="white", fg="black",
                                 state=DISABLED, command=self.destroy) \
            .grid(row=10, columnspan=2, pady=5)

        self.pb_circle.step(99.9)
        self.pb_ellipse.step(99.9)
        self.pb_bar.step(99.9)
        self.pb_dots.step(63)


app = Application()
# app = ProgressWindow(15000, 20000, 45000, 36690, 23400)
app.mainloop()
