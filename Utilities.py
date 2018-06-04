import csv
import logging
import os
from datetime import datetime


class Writer:
    def __init__(self, file_name):
        self.file = None
        self.csv_writer = self.initialize_csv_file(file_name)

    def initialize_csv_file(self, file_name):
        self.file = open(file_name, 'w', newline='')

        return csv.writer(self.file, delimiter=',',
                          quotechar='|', quoting=csv.QUOTE_MINIMAL)

    def write_row_to_file(self, row, file_type='.csv'):
        if file_type == '.csv':
            self.csv_writer.writerow(row)
        else:
            raise Exception("Unknown file type!")


class Cleaner:
    @staticmethod
    def clear_folder(folder):
        print('clearing ' + folder + '...')
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
        print('cleared!')

    def clear_output_images(self):
        self.clear_folder('images/Bars')
        self.clear_folder('images/Circles')
        self.clear_folder('images/Dots')
        self.clear_folder('images/Ellipses')
        self.clear_folder('images/Popcorn')
        # self.clear_folder('images/buffer')


class Logger:
    def __init__(self, log_file_name):
        self.logger = logging.getLogger('FigureGenerator')
        self.logger.setLevel(logging.DEBUG)

        log_file = logging.FileHandler('logs/'+log_file_name)
        self.logger.addHandler(log_file)

    def write_log(self, prompt="", value=""):
        log_string = str(datetime.now()) + "\t\t" + str(prompt) + str(value)
        self.logger.debug(log_string)

