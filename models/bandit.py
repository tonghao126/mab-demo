# Define a bandit object
class Bandit:
    def __init__(self, bandit_probs, name):
        self.bandit_probs = bandit_probs
        self.a = 0
        self.b = 0
        self.name = name

    def pull(self):
        if random.rand() <= self.bandit_probs:
            return 1
        else:
            return 0
