class GameBrain:
    def __init__(self, turtle_group):
        self.turtle_group = turtle_group

    def guess_winner(self, bet, winner):
        """Check if the bet and the winner are matched or not. Then prompt the result."""
        if bet == winner:
            print(f"Great guess, you've won!! The {winner} turtle is the winner!!😎😎😎")
        else:
            print(f"Uhhh 😌😌, you might need another try!! The {winner} turtle is the winner!!")
