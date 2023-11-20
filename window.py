import customtkinter as ctk
from tkinter import CENTER
from settings import *

ctk.set_appearance_mode(DEFAULT_APPEARANCE)
ctk.set_default_color_theme(DEFAULT_COLOR_THEME)

win = ctk.CTk()
win.title("Spending Tracker")
win.geometry(f"{WIDTH}x{HEIGHT}")

# button = ctk.CTkButton(master=win, text="Submit")
# button.place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()