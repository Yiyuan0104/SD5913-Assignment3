"""
Calculator.py - Reserved file for implementing additional features.
"""

def calculator():
    print("Simple Calculator (supports +, -, *, /)")
    while True:
        expr = input("Enter expression (or 'quit' to exit): ")
        if expr.strip().lower() == 'quit':
            print("Goodbye!")
            break
        try:
            # Only allow numbers and operators
            allowed = set('0123456789+-*/.() ')
            if not set(expr).issubset(allowed):
                raise ValueError("Invalid characters in expression.")
            result = eval(expr, {"__builtins__": None}, {})
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
