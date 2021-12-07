import numpy as np
from numpy.core.fromnumeric import size 
import pygame
import sys
import math
from computer import get_computer_decision,COMPUTER_VALUE, PLAYER_VALUE
import library as lb
import time


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
tree_show=False
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

def draw_board(board,player_score,agent_score,tree_show,tree_button):
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
    pygame.draw.rect(screen, [255, 0, 0], tree_button)  # draw button
    pygame.display.update()
    if tree_show ==False:
        text_tree = font.render('Show the tree', True, GREEN, BLUE)
    else :
        text_tree = font.render('hide the tree', True, GREEN, BLUE)
    textRectTree = text_tree.get_rect()
    textRectTree.center = (230, 625)
    screen.blit(text_tree, textRectTree)
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
size=(width,hight+120)
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
tree_button = pygame.Rect(153, 610, 150, 30) #default button

draw_board(board,0,0,tree_show,tree_button)
pygame.display.update()
posX= 0
while True:

    if turn == 0 and not game_over:
        pygame.draw.circle(screen,RED,(posX, int(SQUARESIZE/2)), radius=radius)
    elif turn == 1 and not game_over:
        pygame.draw.circle(screen, YELLOW, (posX, int(SQUARESIZE/2)), radius)
    pygame.display.update()
    if game_over:
        pygame.draw.circle(screen,BLACK,(posX, int(SQUARESIZE/2)), radius=radius)
        if lb.get_score(np.flip(board,0),PLAYER_VALUE)>lb.get_score(np.flip(board,0),COMPUTER_VALUE):
            text_winner = font.render('Player Win  : '+str(lb.get_score(np.flip(board,0),PLAYER_VALUE)), True, GREEN, BLUE)
        else:
            text_winner = font.render('Agent Win  : '+str(lb.get_score(np.flip(board,0),COMPUTER_VALUE)), True, GREEN, BLUE)
        textRect_winner = text_winner.get_rect()
        textRect_winner.center = (240, 30)
        screen.blit(text_winner, textRect_winner)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
        if event.type==pygame.MOUSEMOTION and not game_over:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            mouse_click=event.pos
            posX=mouse_click[0]      
            if turn == 0:
                pygame.draw.circle(screen,RED,(posX, int(SQUARESIZE/2)), radius=radius)
            else :
                pygame.draw.circle(screen, YELLOW, (posX, int(SQUARESIZE/2)), radius)    
        pygame.display.update()            
                
        if event.type==pygame.MOUSEBUTTONDOWN:
            if tree_button.collidepoint(mouse_click):
                if tree_show==False :

                    # add the code for shown the tree
                    tree_show=True
                elif tree_show==True:
                    # add the code for hide the tree
                    tree_show=False  
                draw_board(board,lb.get_score(np.flip(board,0),PLAYER_VALUE),lb.get_score(np.flip(board,0),COMPUTER_VALUE),tree_show,tree_button)
                continue 
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
            draw_board(board,lb.get_score(np.flip(board,0),PLAYER_VALUE),lb.get_score(np.flip(board,0),COMPUTER_VALUE),tree_show,tree_button)    

            if lb.is_state_complete(np.flip(board,0)):
                game_over = True


