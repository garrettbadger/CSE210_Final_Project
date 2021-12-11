from game.actor import Actor

class Score(Actor):
    def __init__(self):
        super().__init__()
        self.score_counter = 0

    def set_score(self, score):
        self.score_counter += score

    def get_score(self):
        return self.score_counter
