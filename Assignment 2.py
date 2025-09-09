# Assignment 2 - Python Programs

# 1. Program to check Leap Year
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a Leap Year"
    else:
        return f"{year} is NOT a Leap Year"

# 2. Simple Calculator
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator"

# 3. Program to assign Grade based on marks
def find_grade(marks):
    if marks >= 85:
        return "Grade: A"
    elif marks >= 70:
        return "Grade: B"
    elif marks >= 50:
        return "Grade: C"
    else:
        return "Grade: F"

# -----------------------------
# Example runs:
if __name__ == "__main__":
    print(check_leap_year(2024))   # Leap Year example
    print(calculator(10, 5, '+'))  # Calculator example
    print(find_grade(72))          # Grade example
