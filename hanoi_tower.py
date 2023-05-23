from problem import *
from collections import namedtuple

State=namedtuple("State", ["disk","rod_from", "rod_to"])


class Hanoi(Problem):
    def __init__(self, n):
        self.size = n
        super().__init__("1" * n, ["3" * n])

    def actions(self, state):
        acts = []
        smallest_disk_rod_1 = state.find("1") + 1
        smallest_disk_rod_2 = state.find("2") + 1
        smallest_disk_rod_3 = state.find("3") + 1

        if smallest_disk_rod_1 == 0:
            smallest_disk_rod_1 = float('inf')
        if smallest_disk_rod_2 == 0:
            smallest_disk_rod_2 = float('inf')
        if smallest_disk_rod_3 == 0:
            smallest_disk_rod_3 = float('inf')

        # if smallest_disk_rod_1 < smallest_disk_rod_2:
        #     acts.append(State(smallest_disk_rod_1,"1", "2"))
        # if smallest_disk_rod_1 < smallest_disk_rod_3:
        #     acts.append(State(smallest_disk_rod_1,"1", "3"))
        # if smallest_disk_rod_2 < smallest_disk_rod_1:
        #     acts.append(State(smallest_disk_rod_2,"2", "1"))
        # if smallest_disk_rod_2 < smallest_disk_rod_3:
        #     acts.append(State(smallest_disk_rod_2,"2", "3"))
        # if smallest_disk_rod_3 < smallest_disk_rod_1:
        #     acts.append(State(smallest_disk_rod_3,"3", "1"))
        # if smallest_disk_rod_3 < smallest_disk_rod_2:
        #     acts.append(State(smallest_disk_rod_3,"3", "2"))

        disk_places = [smallest_disk_rod_1, smallest_disk_rod_2, smallest_disk_rod_3]
        for i in range(3):
            for j in range(3):
                if disk_places[i] < disk_places[j] and i != j:
                    acts.append(State(disk_places[i], i + 1, j + 1))
        return acts

    def result(self, state, action):
        disk, from_rod, to_rod = action
        return state[0:disk - 1] + to_rod + state[disk:]


if __name__ == '__main__':
    h = Hanoi(3)
    print(h.initial, h.goal)
    print(h.actions('213'))
    print(h.result('213', State(1, '2', '1')))