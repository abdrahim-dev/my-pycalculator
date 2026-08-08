import customtkinter as ctk


class CalculatorGuiApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.configure(fg_color="grey20")

        button_layout = [
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "÷"],
        ]

        self.display = ctk.CTkEntry(self, justify="right")  # Create a display entry widget for the calculator
        self.display.grid(row=0,                            # create a grid layout for the display at the top of the window
                          column=0, 
                          columnspan=4, 
                          padx=5, 
                          pady=5, 
                          sticky="nsew") 

        for row_index, row in enumerate(button_layout):     # Loop through the button layout to create buttons for each row and column
            for col_index, button_text in enumerate(row):
                button = ctk.CTkButton(
                    self,
                    width=50,
                    height=50,
                    text=button_text,
                    command=lambda bt=button_text: print(f"{bt} pressed"),
                )
                button.grid(row=row_index + 1,              # create a grid layout for the buttons below the display
                            column=col_index, 
                            padx=5, 
                            pady=5, 
                            sticky="nsew")

if __name__ == "__main__":       
    app = CalculatorGuiApp()
    app.display.insert(0, "0")  # Initialize the display with "0"
    app.mainloop()