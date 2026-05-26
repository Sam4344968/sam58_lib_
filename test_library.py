import pytest
from my_library import hello, add, reverse_string, is_palindrome


def test_hello():
    assert hello("Alice") == "Hello, Alice!"
    assert hello("World") == "Hello, World!"

def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.5, 0.5) == 1.0

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_reverse_string_type_error():
    with pytest.raises(TypeError):
        reverse_string(42)

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama".replace(" ", "")) is True
