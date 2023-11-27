from customtkinter import *
from settings import *
from ctk_custom import *
from PIL.Image import open as open_image
from datetime import datetime
from os import getcwd, chdir
from os.path import join, dirname
from time import sleep
set_appearance_mode(DEFAULT_APPEARANCE)
set_default_color_theme(DEFAULT_COLOR_THEME)

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

#######################################################
##                      Sidebar                      ##
#######################################################
class sidebar_frame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #load images
        chdir(dirname(__file__))
        # home icon
        self.home_ico = CTkImage(dark_image=open_image(join(getcwd(), "img/home.png")))

        # sidebar dimensions
        self.sidebar = CTkFrame(window, width=WIDTH//5-25, height=HEIGHT//5*4, fg_color="#2b2b2b")
        self.sidebar.grid(row=0, column=0, sticky=(SE))

        # disable scaling based on widgets in sidebar
        self.sidebar.grid_propagate(False)

        self.sidebar_buttons_list = [
            # home button
            (CTkButton(window, text="Home", image=self.home_ico,
                        command=home_frame.show_home, font=OPTION,
                        fg_color="#201c1c"), (0.015, 0.11, "w")),
            
            # MyWallet button
            (CTkButton(self, text="MyWallet",
                    font=OPTION, command=wallet_frame.show_wallet,
                    fg_color="#2b2b2b"), (0.5, 0.11, CENTER)),
            
            # spending button
            (CTkButton(self, text="Spending",
                    font=OPTION, command=spending_frame.show_spending,
                    fg_color="#2b2b2b"), (0.5, 0.22, CENTER))
        ]

        self.sidebar_buttons = ButtonGroup()
        for _ in self.sidebar_buttons_list:
            _[0].place(relx=_[1][0], rely=_[1][1], anchor=_[1][2])
            self.sidebar_buttons.add(_[0])

######################################################
##                    Home Frame                    ##
######################################################

class home_frame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # frame
        self.home_screen = CTkFrame(master=master, width=WIDTH//5*4+25, height=HEIGHT-50)
        self.home_screen.grid(row=0, column=5, sticky=(NSEW))

        # group of home screen elements
        self.home_group = Page(STARTING_UPPER_INDENT, 0.05, self)

        # disable scaling based on widgets in sidebar
        self.grid_propagate(False)

        # greeting
        self.home_title = CTkLabel(self,
                                   font=TITLE, 
                                   text=f"Good {self.get_time_of_day()}!")

        # title of progress bar
        self.spending_progress_bar_title = CTkLabel(self, font=SUBTEXT,
                                                    text="$%.2f / $%.2f spent this week" % (weekly_spending, weekly_budget))

        # progress bar
        self.spending_progress_bar = CTkProgressBar(self, orientation="horizontal",
                                        progress_color="#FFFFFF", width=400, height=20)

        # add transactions
        self.add_recent_transactions = CTkButton(self, font=OPTION, text="Add recent transactions",
                                            command=self.show_spending, fg_color="#2b2b2b")
        
        self.home_group.add_group([self.home_title, self.spending_progress_bar_title, self.spending_progress_bar, self.add_recent_transactions])
    
    def get_time_of_day(self):
            time = datetime.now().hour
            if time < 12:
                return "Morning"
            elif time < 16:
                return "Afternoon"
            elif time < 19:
                return "Evening"
            else:
                return "Night"
                 
    # display spending screen 
    def show_spending(self):
        self.spending_screen.tkraise()

######################################################
##                  MyWallet Frame                  ##
######################################################

class wallet_frame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # frame
        self.wallet_screen = CTkFrame(window, width=WIDTH//5*4, height=HEIGHT)
        self.wallet_screen.grid(row=0, column=5, sticky=(NSEW))

        # group of wallet screen elements
        self.wallet_group = Page(STARTING_UPPER_INDENT, 0.05, self)

        # disable scaling based on widgets in sidebar
        self.wallet_screen.grid_propagate(False)

        self.wallet_title = CTkLabel(self,
                            font=TITLE, text="Good Day!")

        self.wallet_group.add_group([self.wallet_title])
        

######################################################
##                  Spending Frame                  ##
######################################################
class spending_frame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
    
        # frame
        self.spending_screen = CTkFrame(window, width=WIDTH//5*4, height=HEIGHT)
        self.spending_screen.grid(row=0, column=5, sticky=(NSEW))

        # group of wallet screen elements
        self.spending_group = Page(STARTING_UPPER_INDENT, 0.05, self)

        # disable scaling based on widgets in sidebar
        self.grid_propagate(False)

        self.spending_title = CTkLabel(master = self.spending_screen,
                            font=TITLE, text="Spending")

        self.spending_group.add_group([self.spending_title])

    # move spending progress bar smoothly
    def move_spending_progress():
        for i in range(int(weekly_spending/weekly_budget*100)):
            spending_frame.spending_progress_bar.set(i/100+0.01)
            window.update()
            sleep(0.01)


#######################################################
##                Displaying Elements                ##
#######################################################

class window(CTk):
    def __init__(self):
        super().__init__()

        # setup window info
        self.resizable(False, False)
        self.title("Spending Tracker")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        # display home screen
        def show_home():
            home_frame.home_screen.tkraise()
            home_frame.home_title.configure(text=f"Good {home_frame.get_time_of_day()}!")
            home_frame.spending_progress_bar_title.configure(text="$%.2f / $%.2f spent this week" % (weekly_spending, weekly_budget))
            spending_frame.move_spending_progress()

        
        # display wallet screen 
        def show_wallet():
            wallet_frame.wallet_screen.tkraise()

        # place all elements in different groups
        hf = home_frame(self)
        hf.home_group.place_all()
        wallet_frame.wallet_group.place_all()
        spending_frame.spending_group.place_all()

        # display home as the first screen
        show_home()
    
win = window()


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
set_fonts()

win.mainloop()