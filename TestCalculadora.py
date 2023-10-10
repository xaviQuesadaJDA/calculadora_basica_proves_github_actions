import pytest
import calculadora

class TestCalculadora():

    
    def test_suma(self):
        calcu = calculadora.Calculadora()
        assert (calcu.suma(8, 7) == 150)