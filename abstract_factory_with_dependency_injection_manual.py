"""
Abstract Factory with Dependency Injection Example
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

# Client that receives factory via dependency injection
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
    def render(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()
        print(button.paint())
        print(checkbox.paint())

if __name__ == "__main__":
    print("Abstract Factory with Dependency Injection:")
    app = Application(WinFactory())
    app.render()
    app = Application(MacFactory())
    app.render()
