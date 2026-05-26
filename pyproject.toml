"""
my_library - A simple Python utility library.
"""

__version__ = "0.1.0"
__author__ = "Your Name"


def hello(name: str) -> str:
    """Returns a personalized greeting.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.

    Example:
        >>> hello("Alice")
        'Hello, Alice!'
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Adds two numbers together.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.

    Example:
        >>> add(2, 3)
        5
    """
    return a + b


def reverse_string(text: str) -> str:
    """Reverses a string.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.

    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Checks whether a string is a palindrome (case-insensitive).

    Args:
        text: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
