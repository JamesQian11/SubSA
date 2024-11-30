import numpy as np

class Greedy(object):
    def __init__(self, index, budget:int):
        self.index = index
        if budget <= 0 or budget > index.__len__():
            raise ValueError("Illegal budget for optimizer.")
        self.n = len(index)
        self.budget = budget

    def select(self, gain_function, update_state=None):
        assert callable(gain_function)
        if update_state is not None:
            assert callable(update_state)
        selected = np.zeros(self.n, dtype=bool)

        greedy_gain = np.zeros(len(self.index))
        for i in range(sum(selected), self.budget):
            greedy_gain[~selected] = gain_function(~selected, selected)
            current_selection = greedy_gain.argmax()
            selected[current_selection] = True
            greedy_gain[current_selection] = -np.inf
            if update_state is not None:
                update_state(np.array([current_selection]), selected)
        return self.index[selected]