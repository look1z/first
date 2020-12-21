# coding:utf-8
from enum import Enum

N = 15
# 棋盘宽度 15 X 15


class ChessboardState(Enum):
    EMPTY = 0
    # 空编号为0
    BLACK = 1
    # 黑编号为1
    WHITE = 2
    # 白编号为2

