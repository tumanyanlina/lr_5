import tkinter as tk
from functools import partial


class CalculatorState:
    def __init__(self):
        self.first_number = None
        self.operation = None


def get_number(entry: tk.Entry) -> float:
    value = entry.get()
    if value == "":
        raise ValueError("Пустое поле")
    return float(value)


def clear(entry: tk.Entry, state: CalculatorState):
    entry.delete(0, tk.END)
    state.first_number = None
    state.operation = None


def button_click(entry: tk.Entry, number: str):
    entry.insert(tk.END, number)


def set_operation(entry: tk.Entry, state: CalculatorState, op: str):
    try:
        state.first_number = get_number(entry)
        state.operation = op
        entry.delete(0, tk.END)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


def equal(entry: tk.Entry, state: CalculatorState):
    try:
        second = get_number(entry)
        entry.delete(0, tk.END)

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: "Ошибка: /0" if b == 0 else a / b
        }

        if state.operation not in operations or state.first_number is None:
            entry.insert(0, "Ошибка")
            return

        result = operations[state.operation](state.first_number, second)
        entry.insert(0, str(result))

    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


root = tk.Tk()
root.title("Калькулятор")
root.geometry("350x350")
root.resizable(width = False, height = False)
root.configure(bg="ivory3")

state = CalculatorState()

entry = tk.Entry(root, width=25, font=("Arial", 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=15, sticky="ew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for text, row, col in buttons:
    if text.isdigit():
        cmd = partial(button_click, entry, text)
    elif text == "C":
        cmd = partial(clear, entry, state)
    elif text == "=":
        cmd = partial(equal, entry, state)
    else:
        cmd = partial(set_operation, entry, state, text)

    btn = tk.Button(root, text=text, padx=20, pady=15,
                    font=("Arial", 10), bg="ivory", command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
