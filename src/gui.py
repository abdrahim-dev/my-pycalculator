import customtkinter as ctk

from calculator_logic import Calculator


class CalculatorGuiApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.configure(fg_color=("#D3D3D3", "#71797E"))     # (light_mode_color, dark_mode_color)
        self.calculator = Calculator()                          # Create an instance of the Calculator class

        for i in range(5):
            self.grid_columnconfigure(i, weight=1, uniform="col")

        for i in range(6):
            self.grid_rowconfigure(i, weight=1, uniform="row")

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
        ]                                                   # Define the layout of the buttons in a grid format

        self.COLOR_DIGIT = ("#657DC3", "#3E55A2")       # color for digit buttons (light_mode_color, dark_mode_color)
        self.COLOR_OPERATOR = ("#7D65C3", "#593EA2")    # color for operator buttons (light_mode_color, dark_mode_color)
        self.COLOR_ACTION = ("#AB65C3", "#8B3EA2")      # color for AC/⌫ buttons (light_mode_color, dark_mode_color)
        self.COLOR_MODE = ("#779CA6", "#A68177")        # color for light/dark mode toggle button (light_mode_color, dark_mode_color)
        self.COLOR_EQUAL = ("#65C37D", "#3EA25E")       # color for "=" button (light_mode_color, dark_mode_color)

        clear_button = ctk.CTkButton(self, width=50, height=50, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=15, fg_color=self._get_button_color("AC"), text="AC", command=lambda: self.on_button_click("AC"))

        backspace_button = ctk.CTkButton(self, width=50, height=50, font=ctk.CTkFont(size=20, weight="bold"), corner_radius=15, fg_color=self._get_button_color("⌫"), text="⌫", command=lambda: self.on_button_click("⌫"))

        light_dark_button = ctk.CTkButton(self, width=20, height=20, font=ctk.CTkFont(size=12, weight="normal"), corner_radius=10, fg_color=self._get_button_color("☾☀︎"), text="☾☀︎", command=lambda: self.change_appearance_mode())

        # Create a display entry widget for the calculator
        self.display = ctk.CTkEntry(self, justify="right", font=ctk.CTkFont(size=32, weight="bold"), corner_radius=10)

        # create a grid layout for the buttons below the display
        clear_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
        # create a grid layout for the buttons below the display
        backspace_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
        # create a grid layout for the buttons below the display
        light_dark_button.grid(row=0, column=4, padx=5, pady=5, sticky="nsew")
        # create a grid layout for the display at the top of the window
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew") 

        self._update_display()                              # Initialize the display with the current input or result

        for row_index, row in enumerate(button_layout):     # Loop through the button layout to create buttons for each row and column
            for col_index, button_text in enumerate(row):
                button = ctk.CTkButton(
                    self,
                    width=50,
                    height=50,
                    font=ctk.CTkFont(size=20, weight="bold"),
                    corner_radius=15,
                    fg_color=self._get_button_color(button_text),  # Set the button color based on its type 
                    text=button_text,
                    command=lambda bt=button_text: self.on_button_click(bt), # Call the on_button_click method with the button text when clicked
                )
                button.grid(row=row_index + 1,                     # create a grid layout for the buttons below the display
                            column=col_index, 
                            padx=5, 
                            pady=5, 
                            sticky="nsew")

    def on_button_click(self, button_text: str) -> None:           # Handle button clicks and call the appropriate methods in the Calculator class
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

    def _get_button_color(self, button_text: str) -> tuple: # returns a tuple of (light_mode_color, dark_mode_color) based on the button type
        if button_text in self.OPERATOR_SYMBOLS:
            return self.COLOR_OPERATOR
        elif button_text.isdigit() or button_text == ".":
            return self.COLOR_DIGIT
        elif button_text in ["AC", "⌫"]:
            return self.COLOR_ACTION  
        elif button_text == "=":
            return self.COLOR_EQUAL
        else:
            return self.COLOR_MODE 

    def change_appearance_mode(self) -> None:     # Toggle between light and dark mode
        current_mode = ctk.get_appearance_mode()  # returns "Light" or "Dark"
        if current_mode == "Light":
            new_mode = "Dark"
        else:
            new_mode = "Light"
        ctk.set_appearance_mode(new_mode)

    def _format_number(self, value: float) -> str: # Format the number to remove unnecessary decimal points and trailing zeros
        if value.is_integer():
            return str(int(value))
        else:
            return str(value)

    def _update_display(self) -> None:                                           # Update the display with the current input or results
        if self.calculator.current_input:
            self.display.delete(0, ctk.END)                                      # Clear the display
            self.display.insert(0, self.calculator.current_input)                # Update the display with the current input
        else:
            self.display.delete(0, ctk.END)                                      # Clear the display
            self.display.insert(0, self._format_number(self.calculator.result))  # Update the display with the formatted result

if __name__ == "__main__":       
    app = CalculatorGuiApp()
    app.mainloop()