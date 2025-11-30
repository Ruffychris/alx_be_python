def safe_divide(numerator, denominator):
    """
    Safely divides numerator by denominator.
    Handles division by zero and non-numeric inputs.

    Parameters:
        numerator (str or float): The numerator.
        denominator (str or float): The denominator.

    Returns:
        str: Result of the division or error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
