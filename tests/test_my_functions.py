import pytest
import time
import source.my_functions as my_functions

def test_add():
    result  = my_functions.add( num1 = 5 , num2 = 6)
    assert result == 11

def test_add_strings():
    result = my_functions.add(num1 ="two" , num2= "one")
    assert result == "twoone"

def test_divide():
    result = my_functions.divide(num1 = 10, num2 = 5)
    assert result == 2

def test_division_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(num1 = 10, num2 = 0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(num1 = 10, num2 = 5)
    assert result == 2


@pytest.mark.skip(reason = "This feature is currently broken")#for skipping tests
 
def test_add():
    assert my_functions.add(num1= 1 , num2= 2) == 3

@pytest.mark.xfail(reason= "we know we cannot divide by 0" )
def test_divide_zero_brokken():
    my_functions.divide(num1= 4, num2= 0)