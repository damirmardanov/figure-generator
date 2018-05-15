from abc import ABC, abstractstaticmethod, abstractclassmethod


class Figure(ABC):
    @abstractstaticmethod
    def generate(xy, width=0, height=0, angle=0):
        pass

    @abstractclassmethod
    def generate_random(cls):
        pass


class Figures(ABC):
    @abstractstaticmethod
    def generate(xy, count=0):
        pass

    @abstractclassmethod
    def generate_random(cls, count=0):
        pass
