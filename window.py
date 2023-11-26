from customtkinter import *
from settings import *
from ctk_custom import *
from PIL import Image, ImageTk
from datetime import datetime
from time import sleep

# appearance settings
set_appearance_mode(DEFAULT_APPEARANCE)
set_default_color_theme(DEFAULT_COLOR_THEME)

# setup window info
win = CTk()
win.resizable(False, False)
win.title("Spending Tracker")
win.geometry(f"{WIDTH}x{HEIGHT}")

######################################################

# display home screen
def show_home():
    home_screen.tkraise()
    home_title.configure(text=f"Good {get_time_of_day()}!")
    spending_title.configure(text="$%.2f / $%.2f spent this week" % (weekly_spending, weekly_budget))
    move_spending_progress()

# move spending progress bar smoothly
def move_spending_progress():
    for i in range(int(weekly_spending/weekly_budget*100)):
        spending_progress.set(i/100+0.01)
        win.update()
        sleep(0.01)
   
# display wallet screen 
def show_wallet():
    wallet_screen.tkraise()
    
def get_time_of_day():
    time = datetime.now().hour
    if time < 12:
        return "Morning"
    elif time < 16:
        return "Afternoon"
    elif time < 19:
        return "Evening"
    else:
        return "Night"

############################################################
##                      Text Options                      ##
############################################################

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

# set fonts for custom classes in ctk_custom.py             
set_fonts()

#######################################################
##                      Sidebar                      ##
#######################################################

# sidebar dimensions
sidebar = CTkFrame(win, width=WIDTH//5-25, height=HEIGHT//5*4, fg_color="#2b2b2b")
sidebar.grid(row=0, column=0, sticky=(SE))

# disable scaling based on widgets in sidebar
sidebar.grid_propagate(False)

sidebar_buttons_list = [
    # home button
    (CTkButton(master=sidebar, text="Home",
                command=show_home, font=OPTION,
                fg_color="#2b2b2b"), (0.5, 0.11, CENTER)),
    
    # MyWallet button
    (CTkButton(master=sidebar, text="MyWallet",
              font=OPTION, command=show_wallet,
              fg_color="#2b2b2b"), (0.5, 0.22, CENTER)),
    
    # spending button
    (CTkButton(master=sidebar, text="Spending",
              font=OPTION,
              fg_color="#2b2b2b"), (0.5, 0.33, CENTER))
]

sidebar_buttons = ButtonGroup()
for _ in sidebar_buttons_list:
    _[0].place(relx=_[1][0], rely=_[1][1], anchor=_[1][2])
    sidebar_buttons.add(_[0])

######################################################
##                    Home Frame                    ##
######################################################

# frame
home_screen = CTkFrame(master=win, width=WIDTH//5*4+25, height=HEIGHT-50)
home_screen.grid(row=0, column=5, sticky=(NSEW))

# group of home screen elements
home_group = Page(STARTING_UPPER_INDENT, 0.05, home_screen)

# disable scaling based on widgets in sidebar
home_screen.grid_propagate(False)

# greeting
home_title = CTkLabel(master=home_screen,
                      font=TITLE, text=f"Good {get_time_of_day()}!")

# title of progress bar
spending_title = CTkLabel(master=home_screen, font=SUBTEXT,
                          text="$%.2f / $%.2f spent this week" % (weekly_spending, weekly_budget))

# progress bar
spending_progress = CTkProgressBar(master=home_screen, orientation="horizontal",
                                   progress_color="#7e98ba", width=400, height=20)

# add transactions
add_recent_transactions = CTkButton(master=home_screen, font=SUBTEXT,
                                    image=)

Image.Image
home_group.add_group([home_title, spending_title, spending_progress])

######################################################
##                  MyWallet Frame                  ##
######################################################

# frame
wallet_screen = CTkFrame(master=win, width=WIDTH//5*4, height=HEIGHT)
wallet_screen.grid(row=0, column=5, sticky=(NSEW))

# group of wallet screen elements
wallet_group = Page(STARTING_UPPER_INDENT, 0.05, wallet_screen)

# disable scaling based on widgets in sidebar
wallet_screen.grid_propagate(False)

wallet_title = CTkLabel(master=wallet_screen,
                      font=TITLE, text="Good Day!")



wallet_group.add_group([wallet_title])


#######################################################
##                Displaying Elements                ##
#######################################################

# place all elements in different groups
home_group.place_all()
wallet_group.place_all()

# display home as the first screen
show_home()

win.mainloop()