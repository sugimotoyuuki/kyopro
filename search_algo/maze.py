import random

H = 3
W = 4
END_TURN = 4


class MazeState:
    def __init__(self, x, y, points, turn, game_score, evaluated_score):
        self.x = x
        self.y = y
        self.points = points
        self.turn = turn
        self.game_score = game_score
        self.evaluated_score = evaluated_score

    __dx = [1, -1, 0, 0]  # x方向の移動
    __dy = [0, 0, 1, -1]  # y方向の移動

    def new(self, seed):
        self.x = 1
