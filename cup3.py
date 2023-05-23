#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from problem import Problem


class Cup3(Problem):
    def __init__(self):
        # self.initial = (5,0,0)
        # self.goal = (4,1,0)
        super().__init__((5,0,0), [(4,1,0), (4,0,1)])

    def actions(self, state):
        acts = []
        s1, s2, s3 = state
        if s1 > 0 and s2 < 3:
            acts.append("o_1_2")
        if s1 > 0 and s3 < 2:
            acts.append("o_1_3")
        if s2 > 0 and s1 < 5:
            acts.append("o_2_1")
        if s2 > 0 and s3 < 2:
            acts.append("o_2_3")
        if s3 > 0 and s1 < 5:
            acts.append("o_3_1")
        if s3 > 0 and s2 <3:
            acts.append("o_3_2")
        return acts

    def result(self, state, action):
        s1, s2, s3 = state
        action_data = action.split('_')
        _, i, j = action_data

        if int(i) == 1 and int(j) == 2:
            m = min(s1, 3 - s2)
            return s1 - m, s2 + m, s3
        if int(i) == 1 and int(j) == 3:
            m = min(s1, 2 - s3)
            return s1 - m, s2, s3 + m
        if int(i) == 2 and int(j) == 1:
            m = min(s2, 5 - s1)
            return s1 + m, s2 - m, s3
        if int(i) == 2 and int(j) == 3:
            m = min(s2, 2 - s3)
            return s1, s2 - m, s3 + m
        if int(i) == 3 and int(j) == 1:
            m = min(s3, 5 - s1)
            return s1 + m, s2, s3 - m
        if int(i) == 3 and int(j) == 2:
            m = min(s3, 3-s2)
            return s1, s2 + m, s3 - m


    def value(self, state):
        """we have no good heuristics"""
        return 0


if __name__ == '__main__':
    c = Cup3()
    print(c.initial, c.goal)
    print(c.actions(c.initial))
    print(c.result(c.initial, 'o_1_2'))