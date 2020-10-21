import numpy as np
import math
import pygame
import sys
from tkinter import messagebox
from tkinter import *

ROW_COUNT = 6    #Global variables are normally in Mayus to denote they are global
COLUMN_COUNT = 7
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board,row,col,piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[(ROW_COUNT-1)][col] == 0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
def flip_board(board):              #Need to flip the board as (0,0) is at top left corner rather than bottom left
    print(np.flip(board,0))

def winning_move(board, piece):
    #Check all horizontal locations
    for c in range (COLUMN_COUNT - 3):
        for r in range (ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3]== piece:
                return True
    
    #Check all vertical locations
    for c in range (COLUMN_COUNT):
        for r in range (ROW_COUNT -2):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c]== piece:
                return True

    #Check positively sloped diagonals
    for c in range (COLUMN_COUNT -3):
        for r in range (ROW_COUNT -2):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3]== piece:
                return True


    #Check negatively sloped diagonals
    for c in range (COLUMN_COUNT -3):
        for r in range (3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3]== piece:
                return True

def draw_board(board):
    for c in range (COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen, BLACK,(int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE + SQUARESIZE/2)),RADIUS )

    for c in range (COLUMN_COUNT):
        for r in range(ROW_COUNT):   
            if board[r][c] == 1:
                pygame.draw.circle(screen, GREEN,(int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)),RADIUS )
            elif board[r][c] == 2:
                pygame.draw.circle(screen, RED,(int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)),RADIUS )
    pygame.display.update()

board = create_board()
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width,height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


while not game_over:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen,GREEN,(posx,int(SQUARESIZE/2)),RADIUS)
            else:
                pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:


            #Ask for player one input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                #piece == 1
                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,1)

                    if winning_move(board,1):
                        print("Player 1 wins!!! Yayyy")
                        game_over=True
                        winner = 1
                
            #Ask for player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                #piece == 2
                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,2)

                    if winning_move(board,1):
                        print("Player 2 wins!!! Yayyy")
                        game_over=True
                        winner = 2

            
            draw_board(board)
            #flip_board(board)
            

            turn +=1
            turn = turn % 2
            if game_over:
                
                if winner == 1:
                    Tk().wm_withdraw()
                    messagebox.showinfo('Info','Player 1 wins!!!!!')
                else:
                    Tk().wm_withdraw()
                    messagebox.showinfo('Info','Player 2 wins!!!!!')
                
    

