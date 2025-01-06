import tkinter as tk
from tkinter import ttk

class EngineeringCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Engineering Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg="#2E3440")
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#2E3440")
        style.configure("TLabel", background="#2E3440", foreground="#D8DEE9", font=("Helvetica", 12))
        style.configure("TButton", background="#4C566A", foreground="#D8DEE9", font=("Helvetica", 12), borderwidth=1)
        style.map("TButton", background=[("active", "#5E81AC")])

        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=20)

        self.entry = tk.Entry(self.frame, width=40, borderwidth=5, bg="#3B4252", fg="#D8DEE9", insertbackground="#D8DEE9")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '(', ')', 'C'
        ]

        row = 1
        col = 0
        for button in buttons:
            ttk.Button(self.frame, text=button, width=9, command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
        elif button == '=':
            try:
                self.expression = str(self.evaluate_expression(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += button

        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def evaluate_expression(self, expression):
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        def apply_op(a, b, op):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return a / b

        values = []
        operators = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            if expression[i] == '(':
                operators.append(expression[i])
            elif expression[i].isdigit() or expression[i] == '.':
                val = 0
                decimal = False
                decimal_places = 0
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    if expression[i] == '.':
                        decimal = True
                    else:
                        if decimal:
                            decimal_places += 1
                            val = val * 10 + int(expression[i])
                        else:
                            val = val * 10 + int(expression[i])
                    i += 1
                if decimal:
                    val = val / (10 ** decimal_places)
                values.append(val)
                i -= 1
            elif expression[i] == ')':
                while len(operators) != 0 and operators[-1] != '(':
                    val2 = values.pop()
                    val1 = values.pop()
                    op = operators.pop()
                    values.append(apply_op(val1, val2, op))
                operators.pop()
            else:
                while (len(operators) != 0 and precedence(operators[-1]) >= precedence(expression[i])):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = operators.pop()
                    values.append(apply_op(val1, val2, op))
                operators.append(expression[i])
            i += 1

        while len(operators) != 0:
            val2 = values.pop()
            val1 = values.pop()
            op = operators.pop()
            values.append(apply_op(val1, val2, op))

        return values[-1]

if __name__ == "__main__":
    root = tk.Tk()
    app = EngineeringCalculator(root)
    root.mainloop()