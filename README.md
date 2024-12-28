## Overview
This Python script implements a simple GUI-based calculator using the `tkinter` library. The calculator performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features
- **Display**: A text display that shows the current input and the result of calculations.
- **Buttons**: Numeric and operator buttons for input, along with clear (`C`) and equals (`=`) buttons.
- **Interactive GUI**: Real-time updates to the display based on user input.

## How It Works
1. **Input**: Users interact with the numeric and operator buttons to input expressions.
2. **Processing**: The `calculate` function evaluates the expression entered by the user when the `=` button is pressed.
3. **Output**: The result of the calculation is displayed. If an error occurs (e.g., invalid input), the display shows "Error".

## Usage
### Prerequisites
- Python 3.x

### Steps to Run
1. Save the script in a file, e.g., `simple_calculator.py`.
2. Open a terminal or command prompt.
3. Run the script using the command:
   ```
   python simple_calculator.py
   ```
4. Use the buttons in the calculator GUI to perform calculations.

### Example Interaction
- **Input:**
  - Press `7`, `+`, `3`, and `=`.
- **Output:**
  - The display will show `10`.

## Code Structure
### Key Functions
1. **`update_display(value)`**:
   - Updates the display with the button value pressed.
   - Clears the display if the `C` button is pressed.

2. **`calculate()`**:
   - Evaluates the expression currently in the display.
   - Handles errors by displaying "Error".

### Buttons
- **Numeric Buttons (`0-9`)**:
  - Used to input numbers.
- **Operator Buttons (`+`, `-`, `*`, `/`)**:
  - Used to input arithmetic operations.
- **Special Buttons**:
  - `C`: Clears the display.
  - `=`: Evaluates the expression.

## License
This script is provided "as-is" for educational purposes. Feel free to modify and use it in your projects.

