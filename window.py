from customtkinter import *
from settings import *
from ctk_custom import *

# appearance settings
set_appearance_mode(DEFAULT_APPEARANCE)
set_default_color_theme(DEFAULT_COLOR_THEME)

# setup window info
win = CTk()
win.title("Spending Tracker")
win.geometry(f"{WIDTH}x{HEIGHT}")

######################################################
def home_pressed():
    print("Home")

######################################################

# text options
DEFAULT_FONT = CTkFont(
                family="Futura",
                size=20
                )

######################################################

# sidebar dimensions
sidebar = CTkFrame(win, width=WIDTH//5, height=HEIGHT, fg_color="#2b2b2b")
sidebar.grid(row=0, column=0)

# disable scaling based on widgets in sidebar
sidebar.grid_propagate(False)

######################################################

sidebar_buttons_list = [
    CTkButton(master=sidebar, text="Home",
                        command=home_pressed, font=DEFAULT_FONT,
                        fg_color="#2b2b2b")
]

sidebar_buttons = ButtonGroup()
for _ in sidebar_buttons_list:
    _.place(relx=0.1, rely=0.1)
    sidebar_buttons.add(_)
sidebar_buttons.make_clear("#18345c", "#2b2b2b")
















win.mainloop()