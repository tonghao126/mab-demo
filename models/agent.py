# Define an agent object
class Agent:
    def __init__(self, data):
        '''TODO: add UCB
        pass in data, a DataFrame with historical records
        '''
        self.data = data

    def thompson_sampling(self, a, b, n_sample):
        sample = random.beta(a, b, n_sample)
        return sample

    def choose_bandit(self, n_sample=1):
        max = 0
        for bandit_name in self.data:
            a, b = self.data[bandit_name]['data']
            sample_mean = self.thompson_sampling(a, b, n_sample).mean()
            #             print(bandit_name, sample_mean)
            if sample_mean > max:
                max = sample_mean
                winner = bandit_name
        return winner
