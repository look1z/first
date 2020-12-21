#codiing:utf-8
from consts import *
from gobang import GoBang


class GoBangAI(object):
    def __init__(self,gobang):
        self.__gobang = gobang

    def Value(self,direction,i,j):
        value_direction = 0
        value_direction_2 = 0
        axis_count = 1
        black_axis_count = 1
        for (xdirection, ydirection) in direction:
            axis_count += self.__gobang.count_on_direction(i=i, j=j, xdirection=xdirection, ydirection=ydirection, color=ChessboardState.WHITE)
            if axis_count >= 5:
                value_direction = 100000
            if axis_count == 4:
                value_direction = 10000
            if axis_count == 3:
                value_direction = 200
            if axis_count == 2:
                value_direction = 10
            black_axis_count += self.__gobang.count_on_direction(i=i, j=j, xdirection=xdirection, ydirection=ydirection, color=ChessboardState.BLACK)
            if black_axis_count >= 5:
                value_direction_2 = 50000
            if black_axis_count == 4:
                value_direction_2 = 2000
            if black_axis_count == 3:
                value_direction_2 = 150
            if black_axis_count == 2:
                value_direction_2 = 10

        return value_direction+value_direction_2

    def Carry(self):
        directions = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1), (1, -1)], [(-1, -1), (1, 1)]]
        n, m = 0, 0
        bigvalue = 0
        for i in range(0,N):
            for j in range(0,N):
                a = self.__gobang.get_chessboard_state(i, j)
                if self.__gobang.get_chessboard_state(i, j) == ChessboardState.EMPTY:
                    value = 0
                    for direction in directions:
                        value += self.Value(direction=direction, i=i, j=j)

                    if value > bigvalue:
                        bigvalue = value
                        n, m = i, j
        return self.__gobang.set_chessboard_state(i=n, j=m, state=ChessboardState.WHITE)







