import pytest
from project import function_display, differentiate, indef_integrate, def_integrate
from decimal import *
getcontext().prec = 5

def test_function_display():
    assert function_display([{"co": -0.3, "power": 1}, {"co": 9, "power": 0}], 1) == "-0.3x+9"

testList = [{"co": 2, "power": 2}, {"co": -0.3, "power": 1}, {"co": 9, "power": 0}]

def test_differentiate():
    assert differentiate(testList) == "f'(x)=4x-0.30000"

def test_indef_integrate():
    assert indef_integrate(testList) == "∫f(x)dx=0.66667x^3-0.15000x^2+9x+C"

def test_def_integrate():
    assert def_integrate(testList, 1, 2) == Decimal('13.216')
