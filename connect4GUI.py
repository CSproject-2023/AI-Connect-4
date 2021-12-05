import numpy as np
from numpy.core.fromnumeric import size 
import pygame
import sys
import math
from computer import get_computer_decision,COMPUTER_VALUE, PLAYER_VALUE
import library as lb


PLAYER_TURN= 0
COMPUTER_TURN= 1


ROW_COUNT=8
COLUMN_COUNT=8
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
YELLOW=(255,255,0)
alpha_beta=False
clicked=False
def create_board():
    board=np.zeros((ROW_COUNT,COLUMN_COUNT), dtype=np.uint8)
    return board

def drop_piece(board,col,row,piece):
    board[row][col]=piece
    pass

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col]==0
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r


def print_board(board):
    print(np.flip(board,0))

def winning_move(board,piece):
    #check horizontal location for win 
    for c in range (COLUMN_COUNT):
        pass

def draw_board(board,player_score,agent_score):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):        
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), hight-int(r*SQUARESIZE+SQUARESIZE/2)), radius)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), hight-int(r*SQUARESIZE+SQUARESIZE/2)), radius)
    text_player_score = font.render('Player Score : '+str(player_score), True, GREEN, BLUE)
    text_agent_score = font.render('Agent Score : '+ str(agent_score), True, GREEN, BLUE)
    textRect_player_score = text_player_score.get_rect()
    textRect_agent_score = text_agent_score.get_rect()
    textRect_player_score.center = (140, 580)
    textRect_agent_score.center = (320 , 580)
    screen.blit(text_player_score, textRect_player_score)
    screen.blit(text_agent_score, textRect_agent_score)
    pygame.display.update()

def draw_first_sreen():
    pass
board=create_board()
game_over=False
turn =0

pygame.init()

SQUARESIZE=60 #size of each square =100px

width=COLUMN_COUNT*SQUARESIZE
hight=(ROW_COUNT+1)*SQUARESIZE
size=(width,hight+75)
radius=int(SQUARESIZE/2)

screen=pygame.display.set_mode(size)

default_button = pygame.Rect(90, 200, 100, 50) #default button
alpha_beta_button= pygame.Rect(220, 200, 200, 50) #alpha_beta button
font = pygame.font.Font('freesansbold.ttf', 16)

text1 = font.render('Default', True, GREEN, BLUE)
text2 = font.render('with alpha beta pruning', True, GREEN, BLUE)
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect1.center = (140, 225)
textRect2.center = (320 , 225)
while not clicked:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position

            # checks if mouse position is over the button

            if default_button.collidepoint(mouse_pos):
                clicked=True
            if alpha_beta_button.collidepoint(mouse_pos):
                clicked=True    
                alpha_beta=True

        pygame.draw.rect(screen, [255, 0, 0], default_button)  # draw button
        pygame.draw.rect(screen, [255, 0, 0], alpha_beta_button)  # draw button
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        pygame.display.update()

draw_board(board,0,0)
pygame.display.update()

posX= 0
while not game_over:
    
    if turn == 0:
        pygame.draw.circle(screen,RED,(posX, int(SQUARESIZE/2)), radius=radius)
    else :
        pygame.draw.circle(screen, YELLOW, (posX, int(SQUARESIZE/2)), radius)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            pygame.display.update()
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posX=event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen,RED,(posX, int(SQUARESIZE/2)), radius=radius)
            else :
                pygame.draw.circle(screen, YELLOW, (posX, int(SQUARESIZE/2)), radius)    
        pygame.display.update()            
                
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            #player 1 turn 
            if turn ==PLAYER_TURN:
                posX=event.pos[0]
                col=int(math.floor(posX/SQUARESIZE))

                
                if is_valid_location(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,col,row,PLAYER_VALUE)

                    col=get_computer_decision(np.flip(board,0) , alpha_beta)
                    if is_valid_location(board,col):   
                        row=get_next_open_row(board,col)
                        drop_piece(board,col,row,COMPUTER_VALUE)
                    else:
                        sys.exit()



            print_board(board)
            draw_board(board,0,0)    
            if lb.is_state_complete(board):
                game_over= True     

            #player 2 turn 

