import csv
import os


class Writer:
    def __init__(self, file_name):
        self.csv_writer = self.initialize_csv_file(file_name)

    @staticmethod
    def initialize_csv_file(file_name):
        csv_file_name = "C:/Users/Дамир/Desktop/Учеба/Диплом/csv_files/" + file_name + ".csv"
        csv_file = open(csv_file_name, 'w', newline='')
        return csv.writer(csv_file, delimiter=',',
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