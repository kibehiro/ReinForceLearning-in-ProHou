import numpy as np


class Evaluation:

    def __init__(self, grid_world, row, column):
        self.grid_world = grid_world
        self.row = row
        self.column = column

    def evaluation(self, evaluation_agent_span, evaluation_times):

        goal_agent_count = 0

        for i in range(evaluation_times):

            # エージェントの初期配置を設定
            x = np.random.randint(self.row)
            y = np.random.randint(self.column)

            for j in range(evaluation_agent_span):

                if self.grid_world[y][x] == [0] * 4:
                    goal_agent_count += 1
                    break

                # 一番大きい矢印を取得
                max_arrow = max(self.grid_world[y][x])
                # 一番大きい矢印が複数ある場合用の変数
                max_direction = []

                # 一番大き数の方向を取得(複数対応)
                for k, max_num in enumerate(self.grid_world[y][x]):
                    if max_num == max_arrow:
                        max_direction.append(k)

                if len(max_direction) - 1 != 0:
                    direction = np.random.choice(max_direction)  # 一番大きい数の中からランダムで移動
                else:
                    direction = max_direction[0]

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

        print('ゴールした評価エージェントの数は:', goal_agent_count)
