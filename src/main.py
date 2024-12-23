"""
main.py

Bu modül, selamlaşma ve veda işlemleri için Greeter sınıfını içerir.
"""
from datetime import datetime

class Greeter:
    def say_hello(self, name: str) -> str:
        return f"Hello, {name}!"

    def say_goodbye(self, name: str) -> str:
        return f"Goodbye, {name}!"

    def greet_based_on_time(self, name: str) -> str:
        current_hour = datetime.now().hour

        if 5 <= current_hour < 12:
            return f"Good morning, {name}!"
        elif 12 <= current_hour < 18:
            return f"Good afternoon, {name}!"
        elif 18 <= current_hour < 22:
            return f"Good evening, {name}!"
        else:
            return f"Good night, {name}!"
