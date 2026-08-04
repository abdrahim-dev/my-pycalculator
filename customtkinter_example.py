"""
CustomTkinter Demo – overview of the main widgets and styling options
============================================================================
Installation:  pip install customtkinter or uv add customtkinter

Run the script and click through the tabs to see how different
CustomTkinter features look and behave.
The code in each tab is intentionally commented so you can copy
snippets directly for your own calculator.
"""

import customtkinter as ctk

# ---------------------------------------------------------------------------
# 1) BASIC SETTINGS (global, usually at the top of the script)
# ---------------------------------------------------------------------------
# Appearance Mode: "System", "Dark", or "Light"
ctk.set_appearance_mode("Dark")

# Color Theme: "blue" (default), "green", "dark-blue"
# You can also specify a path to a custom .json theme file!
ctk.set_default_color_theme("blue")


class DemoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter Feature-Übersicht")
        self.geometry("650x550")

        # -------------------------------------------------------------
        # TABVIEW – organizes multiple "pages" in one window
        # -------------------------------------------------------------
        self.tabview = ctk.CTkTabview(self, corner_radius=15)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)

        self.tab_buttons = self.tabview.add("Buttons")
        self.tab_inputs = self.tabview.add("Inputs")
        self.tab_controls = self.tabview.add("Slider & Switch")
        self.tab_layout = self.tabview.add("Layout & Colors")

        self.build_buttons_tab()
        self.build_inputs_tab()
        self.build_controls_tab()
        self.build_layout_tab()

    # ===================================================================
    # TAB 1: BUTTONS – different styles, hover effects, corner radius
    # ===================================================================
    def build_buttons_tab(self):
        frame = self.tab_buttons

        ctk.CTkLabel(
            frame, text="Standard-Button", font=ctk.CTkFont(size=14)
        ).pack(pady=(20, 5))

        ctk.CTkButton(
            frame,
            text="Klick mich",
            command=lambda: print("Button geklickt!"),
        ).pack(pady=5)

        ctk.CTkLabel(frame, text="Custom Farben & abgerundete Ecken").pack(
            pady=(20, 5)
        )
        ctk.CTkButton(
            frame,
            text="Custom Style",
            fg_color="#2CC985",       # Background color
            hover_color="#207A54",    # Hover color
            text_color="white",
            corner_radius=20,         # Corner radius
            font=ctk.CTkFont(size=16, weight="bold"),
            width=200,
            height=45,
        ).pack(pady=5)

        ctk.CTkLabel(frame, text="Outline-Style (nur Rahmen)").pack(
            pady=(20, 5)
        )
        ctk.CTkButton(
            frame,
            text="Outline",
            fg_color="transparent",
            border_width=2,
            border_color="#3B8ED0",
            text_color="#3B8ED0",
            hover_color="#1a1a1a",
        ).pack(pady=5)

    # ===================================================================
    # TAB 2: INPUTS – entry field, e.g. for the calculator display
    # ===================================================================
    def build_inputs_tab(self):
        frame = self.tab_inputs

        ctk.CTkLabel(
            frame, text="Entry-Feld (ideal für ein Rechner-Display)"
        ).pack(pady=(20, 5))

        self.display_entry = ctk.CTkEntry(
            frame,
            placeholder_text="0",
            font=ctk.CTkFont(size=28),
            justify="right",           # Right-aligned text, like on real calculators
            width=280,
            height=60,
            corner_radius=10,
        )
        self.display_entry.pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Text ins Display schreiben",
            command=self.write_to_display,
        ).pack(pady=10)

        ctk.CTkLabel(frame, text="Textbox (z.B. für Verlauf/History)").pack(
            pady=(30, 5)
        )
        self.history_box = ctk.CTkTextbox(frame, width=280, height=100)
        self.history_box.pack(pady=5)
        self.history_box.insert("0.0", "12 + 5 = 17\n8 * 3 = 24\n")

    def write_to_display(self):
        self.display_entry.delete(0, "end")
        self.display_entry.insert(0, "42")

    # ===================================================================
    # TAB 3: SLIDER & SWITCH – e.g. for a Dark/Light mode toggle
    # ===================================================================
    def build_controls_tab(self):
        frame = self.tab_controls

        ctk.CTkLabel(frame, text="Switch – z.B. Dark/Light Mode Umschalter").pack(
            pady=(20, 5)
        )
        self.mode_switch = ctk.CTkSwitch(
            frame,
            text="Dark Mode",
            command=self.toggle_mode,
            onvalue="Dark",
            offvalue="Light",
        )
        self.mode_switch.select()  # Initial state: on
        self.mode_switch.pack(pady=5)

        ctk.CTkLabel(frame, text="Slider – z.B. Lautstärke, Schriftgröße").pack(
            pady=(30, 5)
        )
        self.slider = ctk.CTkSlider(
            frame, from_=0, to=100, command=self.on_slider_change
        )
        self.slider.pack(pady=5)
        self.slider_label = ctk.CTkLabel(frame, text="Wert: 50")
        self.slider_label.pack()
        self.slider.set(50)

        ctk.CTkLabel(frame, text="Segmented Button – z.B. Modus wählen").pack(
            pady=(30, 5)
        )
        ctk.CTkSegmentedButton(
            frame, values=["Standard", "Wissenschaftlich", "Programmierer"]
        ).pack(pady=5)

    def toggle_mode(self):
        ctk.set_appearance_mode(self.mode_switch.get())

    def on_slider_change(self, value):
        self.slider_label.configure(text=f"Wert: {int(value)}")

    # ===================================================================
    # TAB 4: LAYOUT & COLORS – grid system like a calculator keypad
    # ===================================================================
    def build_layout_tab(self):
        frame = self.tab_layout

        ctk.CTkLabel(
            frame, text="Grid-Layout – so baust du das Zahlen-Pad auf"
        ).pack(pady=(20, 10))

        button_grid = ctk.CTkFrame(frame, fg_color="transparent")
        button_grid.pack(pady=10)

        # Sample 3x3 number grid, like on a real calculator
        labels = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]
        for row_index, row in enumerate(labels):
            for col_index, label in enumerate(row):
                btn = ctk.CTkButton(
                    button_grid,
                    text=label,
                    width=70,
                    height=70,
                    corner_radius=15,
                    font=ctk.CTkFont(size=20),
                    fg_color="#2b2b2b",
                    hover_color="#3B8ED0",
                )
                # sticky + grid with padding ensures even spacing
                btn.grid(row=row_index, column=col_index, padx=6, pady=6)

        ctk.CTkLabel(
            frame,
            text="Tip: grid_columnconfigure(..., weight=1) makes columns\n"
            "grow evenly when you make the window resizable.",
            justify="left",
            text_color="gray",
        ).pack(pady=(20, 0))


if __name__ == "__main__":
    app = DemoApp()
    app.mainloop()