from customtkinter import *
from settings import *

def set_fonts():
    global OPTION, TITLE, SUBTEXT

    # text options
    OPTION = CTkFont(
                    family="Futura",
                    size=25
                    )

    TITLE = CTkFont(
                    family="Futura",
                    size=30
                    )

    SUBTEXT = CTkFont(
                    family="Futura",
                    size=20
                    )

class ButtonGroup:
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
    
class Page:
    def __init__(self, starting_spacer : int, indent : int, master : CTk = None):
        # spacing options
        self.hdr_space = HEADER_SPACING
        self.ln_space = LINE_SPACING
        self.group_spacing = GROUP_SPACING
        
        # list of attributes in custom group or in whole group
        self.attr_list = []
        self.custom_group = []
        
        # keep track of spacing and indents
        self.spacer = starting_spacer
        self.indent = indent
        
        # master window for attributes to be displayed on
        self.master = master
    
    # add to list of all attributes
    def add_group(self, group : list) -> None:
        self.attr_list.append(group)
    
    # place all attributes on screen
    def place_all(self) -> None:
        for group in self.attr_list:
            for attr in range(len(group)):
                # placing the header/title of the group
                if attr == 0:
                    group[attr].place(relx=self.indent, rely=self.spacer, anchor="w")
                    # avoids adding extra spacing
                    if len(group) > 1:
                        self.spacer += self.hdr_space
                
                # listing elements in the group
                else:
                    group[attr].place(relx=self.indent, rely=self.spacer, anchor="w")
                    # avoids adding extra spacing
                    if len(group) > attr + 1:
                        self.spacer += self.ln_space
            
            # space out groups
            self.spacer += self.group_spacing
    
    def add_to_group(self, attr_type : str, text : str = None, custom_obj = None) -> None:
        # header format
        if attr_type == "header":
            self.custom_group.append(
                CTkLabel(master=self.master, font=TITLE, text=text)
            )
        
        # subtext formatting
        elif attr_type == "subtext":
            self.custom_group.append(
                CTkLabel(master=self.master, font=SUBTEXT, text=text)
            )
        
        # allows user to add custom attributes
        else:
            self.custom_group.append(custom_obj)
            
    
    def add_custom_group(self) -> None:
        self.attr_list.append(self.custom_group)
        # reset group
        self.custom_group = []