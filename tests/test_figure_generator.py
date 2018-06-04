import csv
import os
import cv2
import pytest
import numpy as np

from Converter import Converter
from Main import Application
from Processing import Processing
from Utilities import Writer
from Processing.GaussianNoise import GaussianNoise


class TestValidationCount(object):
    def test_empty(self):
        assert not Application().on_validate_count(P="")

    def test_p_zero(self):
        assert Application().on_validate_count(P="0")

    def test_p_less(self):
        assert Application().on_validate_count(P="2000")

    def test_p_more(self):
        assert not Application().on_validate_count(P="200000")

    def test_value_error(self):
        assert not Application().on_validate_count(P="asjkdhaksdh")

    def test_negative(self):
        assert not Application().on_validate_count(P="-1000")


class TestValidationRes(object):
    def test_validation_res_p_empty(self):
        assert not Application().on_validate_res(P="")

    def test_validation_res_p_zero(self):
        assert Application().on_validate_count(P="0")

    def test_validation_res_p_less(self):
        assert Application().on_validate_count(P="1900")

    def test_validation_res_p_more(self):
        assert not Application().on_validate_count(P="200000")

    def test_validation_res_value_error(self):
        assert not Application().on_validate_count(P="asjkdhaksdh")

    def test_negative(self):
        assert not Application().on_validate_count(P="-1000")


class TestWriter(object):
    def test_correct_name(self):
        file_name = "../images/buffer/training.csv"
        Writer(file_name)
        assert os.path.isfile(file_name)
        os.remove(file_name)

    def test_incorrect_name(self):
        with pytest.raises(OSError):
            Writer("&?akjhdsfksdf.csv")

    def test_insert_row(self):
        file_name = "../images/buffer/training.csv"
        writer = Writer(file_name)
        assert os.path.isfile(file_name)
        writer.write_row_to_file("123")
        writer.file.close()

        file = open(file_name, "r")
        reader = csv.reader(file)
        for row in reader:
            assert row == ['1', '2', '3']
        file.close()
        os.remove(file_name)


class TestConverter(object):
    def test_bar(self):
        result = Converter.convert_image_to_csv_row(
            cv2.imread("../images/buffer/output.png", cv2.IMREAD_GRAYSCALE),
            "Bar"
        )

        assert result[0] == '1'

    def test_circle(self):
        result = Converter.convert_image_to_csv_row(
            cv2.imread("../images/buffer/output.png", cv2.IMREAD_GRAYSCALE),
            "Circle"
        )

        assert result[0] == '2'

    def test_dots(self):
        result = Converter.convert_image_to_csv_row(
            cv2.imread("../images/buffer/output.png", cv2.IMREAD_GRAYSCALE),
            "Dots"
        )

        assert result[0] == '3'

    def test_ellipse(self):
        result = Converter.convert_image_to_csv_row(
            cv2.imread("../images/buffer/output.png", cv2.IMREAD_GRAYSCALE),
            "Ellipse"
        )

        assert result[0] == '4'

    def test_popcorn(self):
        result = Converter.convert_image_to_csv_row(
            cv2.imread("../images/buffer/output.png", cv2.IMREAD_GRAYSCALE),
            "Popcorn"
        )

        assert result[0] == '5'

    def test_something(self):
        result = Converter.convert_image_to_csv_row(
            cv2.imread("../images/buffer/output.png", cv2.IMREAD_GRAYSCALE),
            "Something"
        )

        assert result[0] == '0'


def test_gaussian_noise():
    image = cv2.imread("../images/buffer/output.png", cv2.IMREAD_GRAYSCALE)
    assert not np.array_equal(GaussianNoise.process(image), image)


def test_processing():
    image = cv2.imread("../images/buffer/output.png", cv2.IMREAD_GRAYSCALE)
    assert not np.array_equal(
        Processing.process_image('../images/buffer/new.png'),
        image
    )
