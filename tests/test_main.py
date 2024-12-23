import pytest
from src.main import Greeter

@pytest.fixture
def greeter():
    return Greeter()

def test_say_hello(greeter):
    assert greeter.say_hello("Barış") == "Hello, Barış!"

def test_say_goodbye(greeter):
    assert greeter.say_goodbye("Barış") == "Goodbye, Barış!"

@pytest.mark.parametrize("name, expected", [
    ("Ali", "Hello, Ali!"),
    ("Ayşe", "Hello, Ayşe!"),
    ("Barış", "Hello, Barış!")
])
def test_say_hello_multiple(greeter, name, expected):
    assert greeter.say_hello(name) == expected
