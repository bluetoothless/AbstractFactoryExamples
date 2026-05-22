"""
Abstract Factory with Dependency Injection Framework Example
Requires: dependency-injector (pip install dependency-injector)
"""
from abc import ABC, abstractmethod
from dependency_injector import containers, providers

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

# Application that depends on GUIFactory
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
    def render(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()
        print(button.paint())
        print(checkbox.paint())

# Dependency Injector Container
class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    factory = providers.Selector(
        config.os_type,
        Windows=providers.Factory(WinFactory),
        Mac=providers.Factory(MacFactory),
    )
    application = providers.Factory(Application, factory=factory)

if __name__ == "__main__":
    container = Container()
    container.config.os_type.from_value('Windows')
    print("DI Framework (Windows):")
    app = container.application()
    app.render()
    container.config.os_type.from_value('Mac')
    print("DI Framework (Mac):")
    app = container.application()
    app.render()
