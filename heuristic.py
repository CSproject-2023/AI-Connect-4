from math import tanh, floor


# heuristic class used to find probability of winning at a certain state
class heuristic:
    # constructor for class give width and length for states to solve
    # give also values of scores points given for getting connected pieces
    def __init__(self, width=8, length=8, v=[0, 1, 3, 6, 10]):
        self.width = width
        self.length = length
        v = [-i for i in v]
        zero = [0, 0, 0, 0]
        self.val = [v, [-v[1]] + zero, [-v[2]] + zero, [-v[3]] + zero, [-v[4]] + zero]

    # function to solve state
    def solve(self, state):
        # variables to hold number of available points to score by each player
        self.tot_available_4, self.p1_available_4, self.p2_available_4 = 0, 0, 0
        # variables to hold score of both players
        self.total_score, self.no_4_won_by1, self.no_4_won_by2 = 0, 0, 0

        # to solve move and try cell cell and see if it controlled by a certain player
        for i in range(self.width):
            for j in range(self.length):
                if i + 3 < self.width: self.update_points(state, i, j, 1, 0) # try horizontal line
                if i + 3 < self.width and j + 3 < self.length: self.update_points(state, i, j, 1, 1) # try diagonal line 45 degree
                if i + 3 < self.width and j - 3 >= 0: self.update_points(state, i, j, 1, -1)  # try diagonal line 135 degree
                if j + 3 < self.length: self.update_points(state, i, j, 0, 1) # try vertical line
        if self.tot_available_4 == 0: # if no player can score points at all then it is draw
            return 0
        elif self.p1_available_4 == 0: # if player 1 cant score points then player 2 win
            return -1
        elif self.p2_available_4 == 0: # if player w cant score points then player 2 win
            return 1
        else: # else calculate player with more probability to win
            return tanh((self.total_score / (self.tot_available_4 * -self.val[0][4])) + \
                        floor(self.no_4_won_by1 / (self.p2_available_4 + 0.001)) * 100 + floor(
                self.no_4_won_by2 / (self.p1_available_4 + 0.001)) * -100)

    # function to see if a certain player control a row and updates variables accordingly
    def update_points(self, state, i, j, x, y):
        points = [0, 0, 0]
        for z in range(4): points[state[i + z * x][j + z * y]] += 1
        self.total_score += self.val[points[2]][points[1]]
        if points[1] == 0 and points[2] == 4: self.no_4_won_by1 += 1
        if points[1] == 4 and points[2] == 0: self.no_4_won_by2 += 1
        if points[1] == 0 or points[2] == 0: self.tot_available_4 += 1
        if points[2] == 0: self.p1_available_4 += 1
        if points[1] == 0: self.p2_available_4 += 1
