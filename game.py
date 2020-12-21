#coding:utf-8
from pygame.locals import *
from sys import exit
import pygame
from consts import *
from gobang import GoBang
from render import GameRender
from GoBangAI import GoBangAI

if __name__ == '__main__':
    gobang = GoBang()
    gobangai = GoBangAI(gobang)
    render = GameRender(gobang)
    #ai = GobangAI(gobang, ChessboardState.WHITE)
    result = ChessboardState.EMPTY
    enable_ai = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if render.one_step():
                    result = gobang.get_chess_result()
                else:
                    continue
                if result != ChessboardState.EMPTY:
                    break
                if enable_ai:
                    gobangai.Carry()
                    result = gobang.get_chess_result()
                else:
                    render.change_state()

        render.draw_chess()
        render.draw_mouse()
        if result != ChessboardState.EMPTY:
            render.draw_result(result)

        pygame.display.update()