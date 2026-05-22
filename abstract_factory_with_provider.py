"""
Abstract Factory with Provider Example
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

# Abstract Factory (same as before)
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> 'Button':
        pass
    @abstractmethod
    def create_checkbox(self) -> 'Checkbox':
        pass

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()
    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    def create_checkbox(self):
        return MacCheckbox()

# Provider/Registry
class FactoryProvider:
    @staticmethod
    def get_factory(os_type: str) -> GUIFactory:
        match:
            case "Windows":
                return WinFactory()
            case "Mac":
                return MacFactory()
            case _:
                raise ValueError(f"Unknown OS type: {os_type}")

# Client code

def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())

if __name__ == "__main__":
    print("Abstract Factory with Provider:")
    factory = FactoryProvider.get_factory('Windows')
    client_code(factory)
    factory = FactoryProvider.get_factory('Mac')
    client_code(factory)
