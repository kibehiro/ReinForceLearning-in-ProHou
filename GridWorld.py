import numpy as np


class GridWorld:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.grid_world = []

    def make_grid_world(self):

        self.grid_world = [[0 for i in range(self.row)] for j in range(self.column)]

        # ゴール場所をランダムで決める
        x = np.random.randint(self.row)
        y = np.random.randint(self.column)

        # ゴール場所を指定
        # x = 0
        # y = 0

        print('ゴールの座標:', x, ',', y)

        self.grid_world[y][x] = 1  # ゴールにフラグを立てる

        #
        # GridWorldの各配列は、[左][上][下][右]の順番で扱う
        #

        # 各グリッドに移動確率を配置(初期値1)
        for y in range(self.column):
            for x in range(self.row):
                if self.grid_world[y][x] != 1:
                    self.grid_world[y][x] = [1] * 4
                    # 端のグリッドからそれ以上行けないように
                    if x == 0:  # 左
                        self.grid_world[y][x][0] = 0
                    if y == 0:  # 上
                        self.grid_world[y][x][1] = 0
                    if y == self.column - 1:  # 上
                        self.grid_world[y][x][2] = 0
                    if x == self.row - 1:  # 下
                        self.grid_world[y][x][3] = 0
                else:
                    self.grid_world[y][x] = [0] * 4

        # グリッドの状態を表示
        for i in range(self.column):
            for j in range(self.row):
                # print(i, j, end='')
                print(self.grid_world[i][j], end='')
            print()
        print('----------------------')

    def get_grid_world(self):
        return self.grid_world
