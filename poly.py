from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("textbox")


class DropDownList(UIControl):
    def draw(self):
        print("dropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
# print(isinstance(ddl, UIControl))
textbox = TextBox()

draw([ddl, textbox])
