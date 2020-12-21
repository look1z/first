# coding:utf-8
from enum import Enum
from consts import *


class GoBang(object):
    def __init__(self):
        # 二维数组的棋盘
        self.__chessMap = [[ChessboardState.EMPTY for j in range(N)] for i in range(N)]
        self.__currentI = -1
        self.__currentJ = -1
        self.__currentState = ChessboardState.EMPTY

    def get_chessMap(self):
        return self.__chessMap

    def get_chessboard_state(self,i,j):
        return self.__chessMap[i][j]

    def set_chessboard_state(self,i,j,state):
        self.__chessMap[i][j] = state
        self.__currentI = i
        self.__currentJ = j
        self.__currentState = state

    # 数指定方向棋子数目
    def count_on_direction(self,i,j, xdirection, ydirection, color):
        count = 0
        for step in range(1,5):
            if xdirection !=0 and (j + xdirection * step < 0 or j + xdirection * step >= N):
                break
            if ydirection !=0 and (i + ydirection * step < 0 or i + ydirection * step >= N):
                break
            if self.__chessMap[i + ydirection * step][j + xdirection * step] == color:
                count += 1
            else:
                break
        return count

    def have_five(self,i,j,color):
        # 8个方向连棋
        directions = [[(-1,0),(1,0)],[(0,-1),(0,1)],[(-1,1),(1,-1)],[(-1,-1),(1,1)]]
        # 遍历每个方向
        for axis in directions:
            axis_count = 1
            for (xdirection, ydirection) in axis:
                axis_count += self.count_on_direction(i,j,xdirection,ydirection,color)
                # 判断五子连珠
                if axis_count >= 5:
                    return True

        return False

    #
    def get_chess_result(self):
        if self.have_five(self.__currentI,self.__currentJ,self.__currentState):
            return self.__currentState
        else:
            return ChessboardState.EMPTY