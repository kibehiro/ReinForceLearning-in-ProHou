from Evaluation import Evaluation
from GridWorld import GridWorld
from Learning import Learning


# グリッドワールドの大きさを指定
row = 5
column = 5

LearningAgentSpan = 10  # 学習エージェントの寿命
LearningTimes = 100  # 学習回数
P = 5  # 報酬
T = 10  # 遡る数

EvaluationAgentSpan = 10  # 評価エージェントの寿命
EvaluationTimes = 100  # 試行回数

grid_world = GridWorld(row, column)
grid_world.make_grid_world()

learning = Learning(grid_world.get_grid_world(), row, column)
learning.do_learning(LearningAgentSpan, LearningTimes, P, T)

evaluation = Evaluation(learning.get_grid_world(), row, column)
evaluation.evaluation(EvaluationAgentSpan, EvaluationTimes)
