import pytest
import calculadora

class Test_Calculadora():

    
    def test_suma(self):
        calcu = calculadora.Calculadora()
        assert (calcu.suma(8, 7) == 150)