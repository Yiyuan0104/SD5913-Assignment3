"""
input_ideas_gui.py - GUI for input ideas selection and interaction
"""

import tkinter as tk
from tkinter import simpledialog, messagebox
import datetime

# --- Functions for each idea ---
def word_count():
    text = simpledialog.askstring("Word Count", "Enter a sentence:")
    if text is not None:
        count = len(text.split())
        messagebox.showinfo("Word Count", f"Word count: {count}")

def max_min_numbers():
    nums = simpledialog.askstring("Max/Min Numbers", "Enter numbers separated by spaces:")
    if nums is not None:
        numbers = [float(n) for n in nums.split() if n.replace('.', '', 1).isdigit()]
        if numbers:
            messagebox.showinfo("Max/Min", f"Max: {max(numbers)}\nMin: {min(numbers)}")
        else:
            messagebox.showerror("Error", "No valid numbers entered.")

def weekday_from_date():
    date_str = simpledialog.askstring("Weekday from Date", "Enter a date (YYYY-MM-DD):")
    if date_str is not None:
        try:
            dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            weekday = dt.strftime('%A')
            messagebox.showinfo("Weekday", f"{date_str} is a {weekday}.")
        except Exception:
            messagebox.showerror("Error", "Invalid date format.")

def reverse_sentence():
    text = simpledialog.askstring("Reverse Sentence", "Enter a sentence:")
    if text is not None:
        messagebox.showinfo("Reversed", f"Reversed: {text[::-1]}")

def math_expression():
    expr = simpledialog.askstring("Math Expression", "Enter a math expression (e.g. 2+3*4):")
    if expr is not None:
        try:
            allowed = set('0123456789+-*/.() ')
            if not set(expr).issubset(allowed):
                raise ValueError("Invalid characters.")
            result = eval(expr, {'__builtins__': None}, {})
            messagebox.showinfo("Result", f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

# --- GUI ---
root = tk.Tk()
root.title("Input Ideas Demo")
root.geometry("320x320")
root.resizable(False, False)

label = tk.Label(root, text="Choose an input demo:", font=("Arial", 14))
label.pack(pady=(24,12))

btn1 = tk.Button(root, text="1. Word count", font=("Arial", 12), width=20, command=word_count)
btn1.pack(pady=6)
btn2 = tk.Button(root, text="2. Max/Min numbers", font=("Arial", 12), width=20, command=max_min_numbers)
btn2.pack(pady=6)
btn3 = tk.Button(root, text="3. Weekday from date", font=("Arial", 12), width=20, command=weekday_from_date)
btn3.pack(pady=6)
btn4 = tk.Button(root, text="4. Reverse sentence", font=("Arial", 12), width=20, command=reverse_sentence)
btn4.pack(pady=6)
btn5 = tk.Button(root, text="5. Math expression", font=("Arial", 12), width=20, command=math_expression)
btn5.pack(pady=6)

root.mainloop()
