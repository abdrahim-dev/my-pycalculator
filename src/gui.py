import customtkinter as ctk

from calculator_logic import Calculator


class CalculatorGuiApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.configure(fg_color="grey20")
        self.calculator = Calculator()  # Create an instance of the Calculator class

        self.OPERATOR_SYMBOLS = {
            "+": "+", 
            "-": "-", 
            "x": "*", 
            "÷": "/"
        }                                                   # Define the set of operator symbols

        button_layout = [
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "÷"],
        ]

        clear_button = ctk.CTkButton(self, 
                                     width=50, 
                                     height=50, 
                                     text="AC", 
                                     command=lambda: self.on_button_click("AC")
                                     )
        backspace_button = ctk.CTkButton(self, 
                                         width=50, 
                                         height=50, 
                                         text="⌫", 
                                         command=lambda: self.on_button_click("⌫")
                                         )

        clear_button.grid(row=5,              # create a grid layout for the buttons below the display
                          column=0, 
                          padx=5, 
                          pady=5, 
                          sticky="nsew")
        
        backspace_button.grid(row=5,              # create a grid layout for the buttons below the display
                              column=1, 
                              padx=5, 
                              pady=5, 
                              sticky="nsew")
        
        self.display = ctk.CTkEntry(self, justify="right")  # Create a display entry widget for the calculator
        self.display.grid(row=0,                            # create a grid layout for the display at the top of the window
                          column=0, 
                          columnspan=4, 
                          padx=5, 
                          pady=5, 
                          sticky="nsew") 
        self._update_display()  # Initialize the display with the current input or result

        for row_index, row in enumerate(button_layout):     # Loop through the button layout to create buttons for each row and column
            for col_index, button_text in enumerate(row):
                button = ctk.CTkButton(
                    self,
                    width=50,
                    height=50,
                    text=button_text,
                    command=lambda bt=button_text: self.on_button_click(bt),
                )
                button.grid(row=row_index + 1,              # create a grid layout for the buttons below the display
                            column=col_index, 
                            padx=5, 
                            pady=5, 
                            sticky="nsew")

    def on_button_click(self, button_text: str) -> None:
        if button_text.isdigit() or button_text == ".":
            self.calculator.press_number(button_text)                            # Call the press_number method with the button text
        elif button_text in self.OPERATOR_SYMBOLS:
            self.calculator.press_operator(self.OPERATOR_SYMBOLS[button_text])   # Call the press_operator method with the translated symbol
        elif button_text == "=":
            try:
                self.calculator.press_equals()                                   # Call the press_equals method to perform the calculation
            except ZeroDivisionError:                       
                self.display.delete(0, ctk.END)
                self.display.insert(0, "Not defined")                            # Display an error message for division by zero
                self.calculator.clear()                            
                return
        elif button_text == "AC":                                                # Call the clear method to reset the calculator
            self.calculator.clear()
        elif button_text == "⌫":                                                 # Call the backspace method to remove the last character
            self.calculator.backspace()
        self._update_display()                                                   # runs no matter which branch executed

    def _format_number(self, value: float) -> str:
        if value.is_integer():
            return str(int(value))
        else:
            return str(value)

    def _update_display(self) -> None:
        if self.calculator.current_input:
            self.display.delete(0, ctk.END)                                      # Clear the display
            self.display.insert(0, self.calculator.current_input)                # Update the display with the current input
        else:
            self.display.delete(0, ctk.END)                                      # Clear the display
            self.display.insert(0, self._format_number(self.calculator.result))  # Update the display with the formatted result

if __name__ == "__main__":       
    app = CalculatorGuiApp()
    app.mainloop()