import pytest

from app.calculator import Calculator

class TestCalc :
    def setup(self):
        self.calc = Calculator

    def test_adding_succes(self):
        assert self.calc.adding(self,2,3)== 5

    def test_adding_succes(self):
        assert self.calc.adding(self, 4, 4) == 8

    def test_adding_unsucces(self):
        assert self.calc.adding(self, 2, 1) == 4

    def test_multiply_succes(self):
        assert self.calc.multiply(self,2,3)== 6


    def test_division_succes(self):
        assert self.calc.division(self,6,3)== 2

    def test_subtraction_succes(self):
        assert self.calc.subtraction(self,6,3)== 3




