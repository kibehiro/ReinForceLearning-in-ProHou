import numpy as np


class Learning:

    def __init__(self, grid_world, row, column):
        self.grid_world = grid_world
        self.row = row
        self.column = column

    def do_learning(self, learning_agent_span, learning_times, p, t):

        goal_agent_count = 0

        for i in range(learning_times):

            # エージェントの初期配置を設定
            x = np.random.randint(self.row)
            y = np.random.randint(self.column)

            # 学習履歴を初期化
            step_history = []

            for j in range(learning_agent_span):

                # エージェントの移動確率
                moving_probability = []

                # ゴールしたらループを抜ける
                if self.grid_world[y][x] == [0] * 4:
                    # 報酬を計算
                    self.calc_reward(p, t, step_history)
                    goal_agent_count += 1
                    break

                # 移動確率を計算
                for k in range(len(self.grid_world[y][x])):
                    moving_probability.append(self.grid_world[y][x][k] / sum(self.grid_world[y][x]))

                # 移動方向を決定
                direction = np.random.choice(len(moving_probability), p=moving_probability)

                # 移動する前の位置と方向を記録
                step_history.append([y, x, direction])

                #  0   1   2  3
                # [左][上][下][右]

                if direction == 0:
                    x = x - 1
                elif direction == 1:
                    y = y - 1
                elif direction == 2:
                    y = y + 1
                elif direction == 3:
                    x = x + 1

        for i in range(self.column):
            for j in range(self.row):
                print(self.grid_world[i][j], end='')
            print()
        print('----------------------')
        print('ゴールした学習エージェントの数は:', goal_agent_count)

    def calc_reward(self, p, big_t, step_history):
        # 遡る数がゴールまでの手順より大きかったら入れかえ
        if big_t > len(step_history):
            big_t = len(step_history)

        t = 0

        for i in range(len(step_history) - big_t, len(step_history))[::-1]:
            y = step_history[i][0]
            x = step_history[i][1]
            direction = step_history[i][2]
            self.grid_world[y][x][direction] = int(self.grid_world[y][x][direction] + p * ((big_t - t + 1) / big_t))
            t += 1

    def get_grid_world(self):
        return self.grid_world
