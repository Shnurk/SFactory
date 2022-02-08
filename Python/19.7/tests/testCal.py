
from app.calculator import Calculator

class TestCal:
    def setup(self):
        self.calc = Calculator

    def test_multiply_cor(self):
        assert self.calc.multiply(self,2,0) == 0

    def test_multiply_uncor(self):
        assert self.calc.multiply(self,2,1) != 3

    def test_adding_cor(self):
        assert self.calc.adding(self,2,2) == 4

    def test_subtraction_cor(self):
        assert self.calc.subtraction(self,2,2) == 0

    def test_division_cor(self):
        assert self.calc.division(self,4,2) == 2