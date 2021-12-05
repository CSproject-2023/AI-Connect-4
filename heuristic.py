from math import tanh, floor


class heuristic:
    def __init__(self, width=8, length=8, v=[0, 1, 3, 6, 10]):
        self.width = width
        self.length = length
        v  = [ -i for i in v]
        zero = [0, 0, 0, 0]
        self.val = [v, [-v[1]] + zero, [-v[2]] + zero, [-v[3]] + zero, [-v[4]] + zero]

    def solve(self, state):
        self.tot_available_4, self.p1_available_4, self.p2_available_4 = 0, 0, 0
        self.total_score, self.no_4_won_by1, self.no_4_won_by2 = 0, 0, 0
        for i in range(self.width):
            for j in range(self.length):
                if i + 3 < self.width: self.update_points(state, i, j, 1, 0)
                if i + 3 < self.width and j + 3 < self.length: self.update_points(state, i, j, 1, 1)
                if i + 3 < self.width and j - 3 >= 0: self.update_points(state, i, j, 1, -1)
                if j + 3 < self.length: self.update_points(state, i, j, 0, 1)
        if self.tot_available_4 == 0:return 0
        elif self.p1_available_4 == 0: return 1
        elif self.p2_available_4 == 0: return -1
        else:
            return tanh((self.total_score / (self.tot_available_4 * -self.val[0][4])) + \
                        floor(self.no_4_won_by1 / (self.p2_available_4 + 0.001)) * 100 + floor(self.no_4_won_by2 / (self.p1_available_4 + 0.001)) * -100)

    def update_points(self, state, i, j, x, y):
        points = [0, 0, 0]
        for z in range(4): points[state[i + z * x][j + z * y]] += 1
        self.total_score += self.val[points[2]][points[1]]
        if points[1] == 0 and points[2] == 4: self.no_4_won_by1 += 1
        if points[1] == 4 and points[2] == 0: self.no_4_won_by2 += 1
        if points[1] == 0 or points[2] == 0: self.tot_available_4 += 1
        if points[2] == 0: self.p1_available_4 += 1
        if points[1] == 0: self.p2_available_4 += 1
