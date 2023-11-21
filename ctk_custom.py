from customtkinter import *

class ButtonGroup():
    def __init__(self):
        self.buttons = []
    
    def add(self, button: CTkButton):
        self.buttons.append(button)
    
    """   
    def make_clear(self, enter, leave):
        print(self.buttons)
        for button in self.buttons:
            button.bind("<Enter>", lambda e: button.configure(fg_color=enter))
            button.bind("<Leave>", lambda e: button.configure(fg_color=leave))
    """