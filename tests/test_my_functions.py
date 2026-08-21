import pytest
import source.my_functions as my_functions

def test_add():
    result  = my_functions.add( num1 = 5 , num2 = 6)
    assert result == 11