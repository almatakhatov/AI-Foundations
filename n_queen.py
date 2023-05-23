from problem import *
import numpy as np

class NQueen(Problem):

    def __init__(self, n):
        self.n = n
        initial_board = np.zeros((self.n, self.n), dtype=np.uint8)
        initial_board = self.list_to_tuple(initial_board)
        super().__init__(initial=initial_board)

    def actions(self, state):
        acts = []
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] == 0:
                    acts.append((i + 1, j + 1))
        return acts

    def result(self, state, action):
        i, j = action
        i, j = i - 1, j - 1
        new_state = self.tuple_to_list(state)
        new_state[i][j] = 1
        for k in range(self.n):
            for l in range(self.n):
                if i == k or j == l or abs(i - k) == abs(j - l):
                    if not (i == k and j == l):
                        new_state[k][l] = 2
        return self.list_to_tuple(new_state)

    def goal_test(self, state):
        for i in range(self.n):
            is_queen_in_row = False
            for j in range(self.n):
                if state[i][j] == 1:
                    is_queen_in_row = True
            if not is_queen_in_row:
                return False
        return True

    def tuple_to_list(self, state):
        new_state = []
        for i in range(self.n):
            new_state.append([x for x in state[i][:]])
        return new_state

    def list_to_tuple(self, state):
        new_state = []
        for i in range(self.n):
            new_state.append(tuple([x for x in state[i][:]]))
        return tuple(new_state)


if __name__ == '__main__':
    n_queen = NQueen(4)
    print(n_queen.initial)
    print(n_queen.goal_test([[0,1,0,0], [0,0,0,1], [1,0,0,0], [0,0,1,0]]))
    print(n_queen.actions(n_queen.initial))
    print(n_queen.result(n_queen.initial, (1,1)))