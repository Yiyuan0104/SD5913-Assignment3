"""
input_ideas.py - Interesting input interaction examples
"""

def word_count():
    text = input("Enter a sentence: ")
    print(f"Word count: {len(text.split())}")


def max_min_numbers():
    nums = input("Enter numbers separated by spaces: ")
    numbers = [float(n) for n in nums.split() if n.replace('.', '', 1).isdigit()]
    if numbers:
        print(f"Max: {max(numbers)}, Min: {min(numbers)}")
    else:
        print("No valid numbers entered.")


def weekday_from_date():
    import datetime
    date_str = input("Enter a date (YYYY-MM-DD): ")
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        print(f"Weekday: {dt.strftime('%A')}")
    except Exception:
        print("Invalid date format.")


def reverse_sentence():
    text = input("Enter a sentence: ")
    print(f"Reversed: {text[::-1]}")


def math_expression():
    expr = input("Enter a math expression (e.g. 2+3*4): ")
    try:
        allowed = set('0123456789+-*/.() ')
        if not set(expr).issubset(allowed):
            raise ValueError("Invalid characters.")
        print(f"Result: {eval(expr, {'__builtins__': None}, {})}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Choose an input demo:")
    print("1. Word count")
    print("2. Max/Min numbers")
    print("3. Weekday from date")
    print("4. Reverse sentence")
    print("5. Math expression")
    choice = input("Enter number (1-5): ")
    if choice == '1':
        word_count()
    elif choice == '2':
        max_min_numbers()
    elif choice == '3':
        weekday_from_date()
    elif choice == '4':
        reverse_sentence()
    elif choice == '5':
        math_expression()
    else:
        print("Invalid choice.")
