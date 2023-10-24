import doctest

def check_point(x: float, y: float) -> str:
    """
    Checks if a point (x, y) is inside a given figure.

    Args:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.

    Returns:
        str: A message indicating whether the point is inside the figure or not.

    Examples:
        >>> check_point(0, 0)
        'uz robež līnijas'
        >>> check_point(1, -1)
        'uz robež līnijas'
        >>> check_point(2, 0)
        'uz robež līnijas'
        >>> check_point(1, 0.5)
        'Iekša firgūrā'
        >>> check_point(0.2, -0.9)
        'Iekša firgūrā'
    """
    if x >= 0 and y >= -1 and y <= -1.5 * x + 3:
        if x == 0 or y == 1 or y == -1.5 * x + 3:
            return 'uz robež līnijas'
        else:
            return 'Iekša figūrā'
    else:
        return 'arpus'

doctest.testmod()