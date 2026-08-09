class UnknownOperatorError(Exception): #Custom exception for unknown operators.
    pass   

class Calculator:
    def __init__(self) -> None:
        self.current_input = ""  # The current input string
        self.current_operator = ""  # The current operator
        self.result = 0.0  # The result of the calculation

    def press_number(self, number: float) -> None:
        if "." in self.current_input and str(number) == ".":
            return                          # Prevent multiple decimal points in the current input
        self.current_input += str(number)   # Append the pressed number to the current input

    def press_operator(self, operator: str) -> None:
        if self.current_input: # If there's a current input, apply the previous operator (if any) to the result and the current input
            value = float(self.current_input)
            if self.current_operator:
                self.result = self._apply_operator(self.current_operator, self.result, value)
            else:
                self.result = value
            self.current_input = ""

        self.current_operator = operator  # Set the current operator to the pressed operator

    def _apply_operator(self, operator: str, operand1: float, operand2: float) -> float:
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            if operand2 != 0:
                return operand1 / operand2
            else:
                raise ZeroDivisionError("Division by zero is not allowed.")
        else:
            raise UnknownOperatorError(f"Unknown operator: {operator}")

    def press_equals(self) -> None:
        if self.current_operator and self.current_input:
            try:
                self.result = self._apply_operator(
                    self.current_operator,
                    self.result,
                    float(self.current_input),
                )
            except ValueError:
                raise ValueError("Invalid input. Please enter a valid number.")
            finally:
                self.current_input = ""
                self.current_operator = ""
        else: # If there's no current operator or no current input, just update the result with the current input (if any)
            if self.current_input:
                self.result = float(self.current_input)
                self.current_input = ""

    def backspace(self) -> None:
        self.current_input = self.current_input[:-1]  # Remove the last character from the current input
            
    def clear(self) -> None:
        self.current_input = ""
        self.current_operator = ""
        self.result = 0.0

if __name__ == "__main__":
    
    calc = Calculator()
    calc.press_number(203)
    calc.press_operator("-")   
    calc.press_number(3)
    calc.press_operator("/")   
    calc.press_number(2)
    calc.press_operator("*")   
    calc.press_number(5)
    calc.press_operator("+")   
    calc.backspace()  # Remove the last operator (+)
    calc.press_number(0.25)
    calc.press_equals()
    print(calc.result)      