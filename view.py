import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class View(tk.Tk):
    def __init__(self):

        # Create the main window
        super().__init__()
        self.title("My App")
        self.geometry("155x330")
        self.resizable(False, False)

        # Create the main frame
        self.title = ttk.Label(self, text="Tkinter Dice Game")
        self.title.grid(row=0, column=0, columnspan=2)

        self.spacer1 = ttk.Label(self, text="")
        self.spacer1.grid(row=1, column=0, columnspan=2)

        # Create the balance and bet frames
        self.balance_label = ttk.Label(self, text="Balance:", anchor="w", width=10)
        self.balance_label.grid(row=2, column=0)
        self.balance = tk.DoubleVar()
        self.balance.set(0)
        self.balance_display = ttk.Label(self, textvariable=self.balance)
        self.balance_display.grid(row=2, column=1)

        self.bet_label = ttk.Label(self, text="Bet:", anchor="w", width=10)
        self.bet_label.grid(row=3, column=0)
        self.bet = tk.DoubleVar()
        self.bet.set(1)
        self.bet_spinbox = ttk.Spinbox(self, from_=1, to=1000, textvariable=self.bet, width=10)
        self.bet_spinbox.grid(row=3, column=1)

        self.spacer2 = ttk.Label(self, text="")
        self.spacer2.grid(row=4, column=0, columnspan=2)

        # Create the number and dice frame
        self.number_label = ttk.Label(self, text="Number:", anchor="w", width=10)
        self.number_label.grid(row=5, column=0)
        self.number = tk.IntVar()
        self.number.set(50)
        self.number_display = ttk.Label(self, textvariable=self.number)
        self.number_display.grid(row=5, column=1)

        self.number_slider = ttk.Scale(self, from_=5, to=96, orient=tk.HORIZONTAL,
                                       command=lambda x: self.number.set(round(float(x))), variable=self.number, length=150)
        self.number_slider.grid(row=6, column=0, columnspan=2)

        self.spacer3 = ttk.Label(self, text="")
        self.spacer3.grid(row=7, column=0, columnspan=2)

        # Create the roll frame
        self.roll_button = ttk.Button(self, text="Roll")
        self.roll_button.grid(row=8, column=0, columnspan=2)

        self.roll_result = tk.StringVar()
        self.roll_result.set("0")
        self.roll_result_display = ttk.Label(self, textvariable=self.roll_result)
        self.roll_result_display.grid(row=9, column=0, columnspan=2)

        self.spacer4 = ttk.Label(self, text="")
        self.spacer4.grid(row=10, column=0, columnspan=2)

        # Create the stats frame
        self.wins_label = ttk.Label(self, text="Wins:", justify="right", anchor="w", width=10)
        self.wins_label.grid(row=11, column=0)
        self.wins = tk.IntVar()
        self.wins.set(0)
        self.wins_display = ttk.Label(self, textvariable=self.wins, width=10, anchor="e")
        self.wins_display.grid(row=11, column=1)

        self.losses_label = ttk.Label(self, text="Losses:", justify="right", anchor="w", width=10)
        self.losses_label.grid(row=12, column=0)
        self.losses = tk.IntVar()
        self.losses.set(0)
        self.losses_display = ttk.Label(self, textvariable=self.losses, width=10, anchor="e")
        self.losses_display.grid(row=12, column=1)

        self.spacer5 = ttk.Label(self, text="")
        self.spacer5.grid(row=13, column=0, columnspan=2)

        # Create the reset frame
        self.reset_button = ttk.Button(self, text="Reset")
        self.reset_button.grid(row=14, column=0, columnspan=2)

    def update_view(self):
        player_bankroll = self.controller.get_player_bankroll()

        self.balance.set(player_bankroll)
        self.bet_spinbox.configure(to=player_bankroll)

        self.wins.set(self.controller.get_wins())
        self.losses.set(self.controller.get_losses())
        self.roll_result.set(self.controller.get_roll())

        self.roll_button.configure(state="normal" if player_bankroll > 0 else "disabled")

    def connect(self, controller):
        self.controller = controller
        self.roll_button.configure(command=self.controller.roll)
        self.reset_button.configure(command=self.controller.reset)
        self.update_view()

    def get_bet(self):
        return self.bet.get()

    def get_number(self):
        return self.number.get()

    def show_error(self, message):
        messagebox.showerror("Error", message)
