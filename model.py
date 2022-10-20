import random


class Model:

    def __init__(self, house_edge=0.015, player_bankroll=1000):
        self.house_edge = house_edge
        self.player_bankroll = player_bankroll
        self.wins = 0
        self.losses = 0
        self.roll = 0

    def roll_dice(self):
        return random.choice([i for i in range(1, 101)])

    def calculate_payout(self, bet, win_rate):
        return bet * (1 - self.house_edge) * (1 / (win_rate/100))

    def play(self, bet, number):
        self.roll = self.roll_dice()
        self.player_bankroll -= bet

        if self.roll < number:
            payout = self.calculate_payout(bet, number)
            self.player_bankroll += payout
            self.wins += 1
        else:
            self.losses += 1

        self.player_bankroll = round(self.player_bankroll, 2)

        if self.player_bankroll <= 0:
            return False

        return True
