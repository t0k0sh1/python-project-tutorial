def _validate_numeric_operands(a, b):
    """Validate that operands are numeric and not None or boolean.
    
    Args:
        a: First operand to validate
        b: Second operand to validate
        
    Raises:
        ValueError: If a or b is None, boolean, or not an int/float type
    """
    if a is None or b is None:
        raise ValueError("Arguments cannot be None")
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("Arguments cannot be boolean")
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Arguments must be numeric types (int or float)")


def add(a, b):
    """Add two numbers.

    Args:
        a: A numeric value
        b: A numeric value

    Returns:
        The sum of a and b

    Raises:
        ValueError: If a or b is None, boolean, or not an int/float type
    """
    _validate_numeric_operands(a, b)
    return a + b


def subtract(a, b):
    """Subtract two numbers.

    Args:
        a: A numeric value
        b: A numeric value

    Returns:
        The difference of a and b (a - b)

    Raises:
        ValueError: If a or b is None, boolean, or not an int/float type
    """
    _validate_numeric_operands(a, b)
    return a - b