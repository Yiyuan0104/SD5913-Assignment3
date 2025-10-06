"""
Calculator.py - GUI Calculator using tkinter (More Vertical Spacing).
"""

import tkinter as tk
from tkinter import messagebox

def evaluate_expression(expr):
    try:
        allowed = set('0123456789+-*/.() ')
        if not set(expr).issubset(allowed):
            raise ValueError("Invalid characters in expression.")
        result = eval(expr, {"__builtins__": None}, {})
        return str(result)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Error"

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

def main():
    root = tk.Tk()
    root.title("Calculator")
    root.configure(bg="#f7f7f7")
    center_window(root, 260, 380)
    root.resizable(False, False)

    expr_var = tk.StringVar()

    display = tk.Entry(root, textvariable=expr_var, font=("Arial", 18, "bold"), bd=0, relief=tk.FLAT, justify='right', width=10, bg="#fff", fg="#000")
    display.grid(row=0, column=0, columnspan=4, padx=4, pady=(16,8), ipady=6)

    button_cfg = {
        'font': ("Arial", 14, "bold"),
        'bg': "#e3e3e3",
        'fg': "#000",
        'activebackground': "#d1d1d1",
        'bd': 0,
        'relief': tk.FLAT,
        'highlightthickness': 0,
        'width': 2,
        'height': 1,
    }

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
        ('(', 5, 0), (')', 5, 1)
    ]

    def on_click(char):
        if char == 'C':
            expr_var.set('')
        elif char == '=':
            result = evaluate_expression(expr_var.get())
            if result.startswith("Error"):
                messagebox.showerror("Calculation Error", result)
                expr_var.set('')
            else:
                expr_var.set(result)
        else:
            expr_var.set(expr_var.get() + char)

    for text, row, col in buttons:
        tk.Button(root, text=text, command=lambda t=text: on_click(t), **button_cfg).grid(row=row, column=col, padx=2, pady=10)

    # Wide '=' button at the end of last row, black text for visibility
    tk.Button(root, text='=', command=lambda: on_click('='), font=("Arial", 14, "bold"),
              bg="#4caf50", fg="#000", activebackground="#388e3c", bd=0, relief=tk.FLAT,
              highlightthickness=0, width=5, height=1).grid(row=5, column=2, columnspan=2, padx=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
