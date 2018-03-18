import os


class Utilities:
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
