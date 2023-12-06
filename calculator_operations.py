import math

def evaluate_expression(expression):
    try:
        if expression.endswith("×") or expression.endswith("+") or expression.endswith("-") or expression.endswith("÷") or expression.endswith("^") or expression.endswith("%") or expression.endswith("."):
            return "Error: Incomplete expression"
        
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError:
        return "Error: Invalid input"

def calculate_sin(value):
    try:
        result = math.sin(math.radians(float(value)))
        return result
    except ValueError:
        return "Error: Invalid input"

def calculate_cos(value):
    try:
        result = math.cos(math.radians(float(value)))
        return result
    except ValueError:
        return "Error: Invalid input"

def calculate_tan(value):
    try:
        result = math.tan(math.radians(float(value)))
        return result
    except ValueError:
        return "Error: Invalid input"

def calculate_lg(value):
    try:
        result = math.log10(float(value))
        return result
    except ValueError:
        return "Error: Invalid input"

def calculate_ln(value):
    try:
        result = math.log(float(value))
        return result
    except ValueError:
        return "Error: Invalid input"

def calculate_sqrt(value):
    try:
        result = math.sqrt(float(value))
        return result
    except ValueError:
        return "Error: Invalid input"

def calculate_factorial(value):
    try:
        result = math.factorial(int(value))
        return result
    except ValueError:
        return "Error: Invalid input"

def calculate_reciprocal(value):
    try:
        result = 1 / float(value)
        return result
    except ValueError:
        return "Error: Invalid input"

def calculate_pi(value):
    try:
        if value == "":
            result = math.pi
        else:
            result = float(value) * math.pi
        return result
    except ValueError:
        return "Error: Invalid input"

def calculate_euler(value):
    try:
        if value == "":
            result = math.e
        else:
            result = math.e ** int(value)
        return result
    except ValueError:
        return "Error: Invalid input"
    
