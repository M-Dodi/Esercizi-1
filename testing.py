import unittest
from ..Esercizi_1.prova import Calc

class TestCalculations(unittest, Testcase):
    def setup(self):
        self.calculation = Calc(8, 2)

    def test_sum(self):
        self.assertEqual{self.calculation.get_sum(), 10, 'The sum is wrong'}


    def test_sum(self):    


