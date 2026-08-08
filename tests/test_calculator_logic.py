from src.calculator_logic import Calculator  # noqa: I001
from src.calculator_logic import UnknownOperatorError 
import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_press_number(calculator):
    calculator.press_number(9)
    assert calculator.current_input == "9"


def test_press_operator(calculator):
    calculator.press_number(5)
    calculator.press_operator("+")

    assert calculator.current_operator == "+"
    assert calculator.result == 5.0
    assert calculator.current_input == ""


def test_press_equals_without_operator(calculator):
    calculator.press_number(8)
    calculator.press_equals()

    assert calculator.result == 8.0

def test_press_clear_in_the_middle_of_input(calculator):
    calculator.press_number(4)
    calculator.press_operator("+")
    calculator.press_number(3)
    calculator.clear()

    assert calculator.current_input == ""
    assert calculator.current_operator == ""
    assert calculator.result == 0.0

def test_press_operator_two_times(calculator):
    calculator.press_number(5)
    calculator.press_operator("-")
    calculator.press_operator("*")  # Different operator this time

    assert calculator.current_operator == "*"
    assert calculator.result == 5.0


def test_press_equals_with_pending_operator_no_second_number(calculator):
    calculator.press_number(6)
    calculator.press_operator("+")
    calculator.press_equals()  # Press equals without entering a second number

    assert calculator.current_operator == "+"  # still pending
    assert calculator.result == 6.0             # unchanged

    calculator.press_number(3)
    calculator.press_equals()
    assert calculator.result == 9.0              # now it resolves correctly

def test_division_by_zero(calculator):
    calculator.press_number(10)
    calculator.press_operator("/")
    calculator.press_number(0)

    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        calculator.press_equals()

def test_not_allowed_operator(calculator):
    calculator.press_number(1)
    calculator.press_operator("^")  # Not allowed operator
    calculator.press_number(2)

    with pytest.raises(UnknownOperatorError, match="Unknown operator: \\^"):
        calculator.press_equals()

def test_not_allowed_value(calculator):
    calculator.press_number(3)
    calculator.press_operator("*")  
    calculator.press_number("abc")  # Invalid value

    with pytest.raises(ValueError, match="Invalid input. Please enter a valid number."):
        calculator.press_equals()