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


def test_backspace_functionality(calculator):
    calculator.press_number(123)
    calculator.backspace()  # Remove the last digit (3)
    assert calculator.current_input == "12"

    calculator.backspace()  # Remove the last digit (2)
    assert calculator.current_input == "1"

    calculator.backspace()  # Remove the last digit (1)
    assert calculator.current_input == ""  # Should be empty now

    calculator.backspace()  # Backspace on empty input should do nothing
    assert calculator.current_input == ""  # Still empty


def test_backspace_does_not_touch_pending_operator(calculator):
    calculator.press_number(5)
    calculator.press_operator("+")
    # current_input is now "" (cleared by press_operator), current_operator is "+"
    calculator.backspace()
    
    assert calculator.current_operator == "+"  # untouched
    assert calculator.result == 5.0             # untouched
    assert calculator.current_input == ""        # still empty, no crash
    

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


def test_press_number_allows_single_decimal_point(calculator):
    calculator.press_number("1")
    calculator.press_number(".")
    calculator.press_number("5")
    assert calculator.current_input == "1.5"


def test_press_number_prevents_multiple_decimal_points(calculator):
    calculator.press_number("1")
    calculator.press_number(".")
    calculator.press_number("5")
    calculator.press_number(".")  # should be ignored
    assert calculator.current_input == "1.5"

def test_press_number_prevents_multiple_points(calculator):
    calculator.press_number("1")
    calculator.press_number(".")
    calculator.press_number(".")  # should be ignored
    assert calculator.current_input == "1."  # still only one decimal point

def test_press_minus_first_number(calculator):
    calculator.press_operator("-")  # Start with a minus operator
    calculator.press_number("3")
    calculator.press_equals()
    assert calculator.result == -3.0

def test_minus_operations_with_negative_numbers(calculator):
    calculator.press_operator("-")  # Start with a minus operator
    calculator.press_number("3")
    calculator.press_operator("-")  # Subtracting a negative number
    calculator.press_number("2")
    calculator.press_equals()
    assert calculator.result == -5.0
