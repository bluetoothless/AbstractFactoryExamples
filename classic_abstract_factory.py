"""
Classic Abstract Factory Example
"""
from abc import ABC, abstractmethod

# Product Interfaces
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Concrete Products
class WinButton(Button):
    def paint(self):
        return "Render a button in Windows style"

class MacButton(Button):
    def paint(self):
        return "Render a button in Mac style"

class WinCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in Windows style"

class MacCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in Mac style"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()
    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client code

def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())

if __name__ == "__main__":
    print("Classic Abstract Factory:")
    client_code(WinFactory())
    client_code(MacFactory())
