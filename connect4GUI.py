import numpy as np
from numpy.core.fromnumeric import size 
import pygame
import sys
import math
from computer import get_computer_decision,COMPUTER_VALUE, PLAYER_VALUE,computer_k
import library as lb
import time

#some constant we will use 
PLAYER_TURN= 0
COMPUTER_TURN= 1

#diminsions of the board
ROW_COUNT=8
COLUMN_COUNT=8
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
YELLOW=(255,255,0)
#some boolean variable to provide charactristics
alpha_beta=False
clicked=False
tree_show=False
#function to make the intial board
def create_board():
    board=np.zeros((ROW_COUNT,COLUMN_COUNT), dtype=np.uint8)
    return board
#function to drop the piece in it's right place 
def drop_piece(board,col,row,piece):
    board[row][col]=piece
    pass
#check if the user put it in valid location 
def is_valid_location(board,col):
    return board[ROW_COUNT-1][col]==0
#get the first zero in the column     
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r


# def print_board(board):
#     print(np.flip(board,0))

def winning_move(board,piece):
    #check horizontal location for win 
    for c in range (COLUMN_COUNT):
        pass
#main function of the program that draw the board on every urn it take matrix of the board and score and tree and button to show it 
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
    #check if we want to show the tree or not 
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

width=COLUMN_COUNT*SQUARESIZE  #width of board 
hight=(ROW_COUNT+1)*SQUARESIZE #hight of the board and add some hight to buttons 
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
user_text = ''
  
# create rectangle
input_rect = pygame.Rect(170, 280, 140, 32)
base_font = pygame.font.Font(None, 32)
user_text = ''
  
# create rectangle
  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive
  
active = False
while not clicked:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
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
  
    if active:
        color = color_active
    else:
        color = color_passive
          
    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)
      
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()


tree_button = pygame.Rect(153, 610, 150, 30) #default button

draw_board(board,0,0,tree_show,tree_button)
pygame.display.update()
posX= 0
computer_k(int(user_text))
while True:
    if not game_over:
        pygame.draw.circle(screen,RED,(posX, int(SQUARESIZE/2)), radius=radius)
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
                tree_show= not tree_show
                draw_board(board,lb.get_score(np.flip(board,0),PLAYER_VALUE),lb.get_score(np.flip(board,0),COMPUTER_VALUE),tree_show,tree_button)
                continue 
            #player 1 turn 
            if turn ==PLAYER_TURN:
                posX=event.pos[0]
                col=int(math.floor(posX/SQUARESIZE))

                
                if is_valid_location(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,col,row,PLAYER_VALUE)

                    col=get_computer_decision(np.flip(board,0) , alpha_beta, tree_show)
                    # print(f"Tree is {tree_show}")
                    if is_valid_location(board,col):   
                        row=get_next_open_row(board,col)
                        drop_piece(board,col,row,COMPUTER_VALUE)
                    else:
                        sys.exit()



            # print_board(board)
            draw_board(board,lb.get_score(np.flip(board,0),PLAYER_VALUE),lb.get_score(np.flip(board,0),COMPUTER_VALUE),tree_show,tree_button)    

            if lb.is_state_complete(np.flip(board,0)):
                game_over = True


