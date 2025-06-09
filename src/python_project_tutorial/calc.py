def add(a, b):
    """Add two numbers.

    Args:
        a: A numeric value
        b: A numeric value

    Returns:
        The sum of a and b

    Raises:
        ValueError: If a or b is not a numeric type or is None
    """
    if a is None or b is None:
        raise ValueError("Arguments cannot be None")
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("Arguments cannot be boolean")
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Arguments must be numeric types (int or float)")
    
    return a + b