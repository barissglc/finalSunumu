import pytest
from src.main import Greeter

@pytest.fixture
def greeter():
    return Greeter()

def test_say_hello(greeter):
    assert greeter.say_hello("Barış") == "Hello, Barış!"

def test_say_goodbye(greeter):
    assert greeter.say_goodbye("Barış") == "Goodbye, Barış!"

def test_personalized_greeting_young(greeter):
    result = greeter.personalized_greeting("Barış", 15)
    assert result == "Hello, Barış! You are so young and full of energy!"

def test_personalized_greeting_adult(greeter):
    result = greeter.personalized_greeting("Barış", 30)
    assert result == "Hello, Barış! You are in the prime of your life!"

def test_personalized_greeting_elder(greeter):
    result = greeter.personalized_greeting("Barış", 65)
    assert result == "Hello, Barış! Wisdom comes with age, doesn't it?"
    


@pytest.mark.parametrize("name, expected", [
    ("Ali", "Hello, Ali!"),
    ("Ayşe", "Hello, Ayşe!"),
    ("Barış", "Hello, Barış!")
])
def test_say_hello_multiple(greeter, name, expected):
    assert greeter.say_hello(name) == expected
