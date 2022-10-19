class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect()

    def connect(self):
        self.view.connect(self)

    def get_player_bankroll(self):
        return self.model.player_bankroll

    def roll(self):
        bet = self.view.get_bet()
        number = self.view.get_number()

        if bet > self.model.player_bankroll:
            self.view.show_error("You don't have enough money to make that bet.")
            return

        self.model.play(bet, number)
        self.view.update_view()

        if self.model.player_bankroll <= 0:
            self.view.show_error("You're out of money!")

    def get_wins(self):
        return self.model.wins

    def get_losses(self):
        return self.model.losses

    def get_roll(self):
        return self.model.roll

    def reset(self):
        self.model.player_bankroll = 1000
        self.model.wins = 0
        self.model.losses = 0
        self.view.update_view()

