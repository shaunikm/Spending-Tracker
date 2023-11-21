from customtkinter import *
from settings import *
from ctk_custom import *
from PIL import Image, ImageTk

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

############################################################
##                      Text Options                      ##
############################################################

# text options
DEFAULT_FONT = CTkFont(
                family="Futura",
                size=25
                )

#######################################################
##                      Sidebar                      ##
#######################################################

# sidebar dimensions
sidebar = CTkFrame(win, width=WIDTH//5, height=HEIGHT, fg_color="#2b2b2b")
sidebar.grid(row=0, column=0)

# disable scaling based on widgets in sidebar
sidebar.grid_propagate(False)

sidebar_buttons_list = [
    (CTkButton(master=sidebar, text="Home",
                command=home_pressed, font=DEFAULT_FONT,
                fg_color="#2b2b2b"), (0.1, 0.1)),
    (CTkButton(master=sidebar, text="MyWallet",
              font=DEFAULT_FONT,
              fg_color="#2b2b2b"), (0.1, 0.2)),
    (CTkButton(master=sidebar, text="Spending",
              font=DEFAULT_FONT,
              fg_color="#2b2b2b"), (0.1, 0.3))
]

sidebar_buttons = ButtonGroup()
for _ in sidebar_buttons_list:
    _[0].place(relx=_[1][0], rely=_[1][1])
    sidebar_buttons.add(_[0])

######################################################
##                    Home Frame                    ##
######################################################














win.mainloop()