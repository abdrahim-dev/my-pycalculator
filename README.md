# my-pycalculator

A desktop calculator built with Python and [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), built as a learning project to practice real-world software engineering workflows: state machine design, test-driven development, Git branching, and GUI/logic separation.

## Features

- **Chained arithmetic** — supports multi-step calculations like `5 - 3 * 2 =`, resolved left-to-right as each new operator is pressed
- **Backspace (⌫)** — remove the last typed digit without clearing the whole entry
- **Clear (AC)** — full reset of the current calculation
- **Sign toggle (+/-)** — flip a number between positive and negative
- **Percentage (%)** — convert a number to its `/100` value (e.g. `50` → `0.5`)
- **Error handling** — division by zero shows a clear "Not defined" message instead of crashing
- **Dark / Light mode toggle** — switch appearance at runtime
- **Clean number formatting** — whole-number results display without a trailing `.0`

## Project structure

```
my-pycalculator/
├── src/
│   ├── calculator_logic.py   # Calculator class — all calculation logic, no GUI dependencies
│   └── gui.py                 # CustomTkinter GUI, wires buttons to Calculator
├── tests/
│   └── test_calculator_logic.py
├── pyproject.toml
├── uv.lock
└── README.md
```

The calculation logic (`Calculator`) is fully independent of the GUI — it has no CustomTkinter imports and can be tested or reused on its own (e.g. behind a different interface).

## Getting started

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency management.

```bash
# Clone the repository
git clone <repo-url>
cd my-pycalculator

# Install dependencies
uv sync

# Run the app
uv run python src/gui.py
```

## Running tests

```bash
uv run pytest
```

Tests cover chained operations, division by zero, unknown operators, backspace, clear, sign toggle, percentage conversion, and decimal-point input validation.

## Tech stack

- Python 3.14
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — GUI
- [pytest](https://docs.pytest.org/) — testing
- [uv](https://docs.astral.sh/uv/) — dependency & environment management

## Design notes

- **Separation of concerns:** `Calculator` (in `calculator_logic.py`) contains zero GUI code — the GUI layer is the only thing that knows CustomTkinter exists.
- **Data-driven button layout:** the digit/operator grid is generated from a small layout structure and a loop, rather than one hardcoded button per line — adding a new button is a data change, not a code change.
- **Custom exceptions:** `UnknownOperatorError` is a dedicated exception type (not a generic `ValueError`), so error handling in the GUI can distinguish between different failure causes without message-string matching.

## Possible future improvements

- Full parenthesized expressions with operator precedence (e.g. `(2 + 3) * 4`)
- Calculation history panel
- Keyboard input support
