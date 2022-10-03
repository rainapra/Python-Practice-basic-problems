#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


# In[2]:


def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[3]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[4]:


def input_player():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)


# In[5]:


input_player()


# In[6]:


player1_marker, player2_marker = input_player()


# In[7]:


def board_marker(board, marker, position):
    board[position] = marker


# In[8]:


board_marker(test_board,'@', 1)
display_board(test_board)


# In[9]:


def win_condition(board, mark):
    return((board[1]== mark and board[2]== mark and board[3]== mark) or 
       (board[4]== mark and board[5]== mark and board[6]== mark) or
       (board[7]== mark and board[8]== mark and board[9]== mark) or
       (board[1]== mark and board[4]== mark and board[7]== mark) or
       (board[2]== mark and board[5]== mark and board[8]== mark) or
       (board[3]== mark and board[6]== mark and board[9]== mark) or
       (board[3]== mark and board[5]== mark and board[7]== mark) or
       (board[1]== mark and board[5]== mark and board[9]== mark))  


# In[10]:


win_condition(test_board, 'X')


# In[11]:


import random

def random_first_choice():
    turn = random.randint(0,1)
    
    if turn == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[15]:


def free_space(board, position):
    return board[position] == ' '


# In[21]:


def board_full(board):
    for s in range(1,10):
        if free_space(board, s):
            return False
    return True


# In[17]:


def player_choice(board):
    
    position =0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not free_space(board, position):
        position = int(input('Enter your position (1-9) :'))
        
    return position


# In[18]:


def replay():
    choice = input('Do you want to play again? Yes or No :')
    return choice == 'Yes'


# In[24]:


print('Welcome to my Tic-Tac-Toe game')

while True:
    
    the_board = [' '] * 10
    player1_marker, player2_marker = input_player()
    
    turn = random_first_choice()
    print(turn + ' will go first')
    
    gameplay = input('Ready to play ?? Select y or n')
    
    if gameplay == 'y':
        gameon = True
    else:
        gameon = False
        
    while gameon:
        
        if turn == 'Player 1':
            
            display_board(the_board)
            
            position = player_choice(the_board)
            
            board_marker(the_board, player1_marker, position)
            
            if win_condition(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has WON!!!')
                gameon = False
            else:
                if board_full(the_board):
                    display_board(the_board)
                    print('Game Tied!!!')
                    break
                else:
                    turn = 'Player 2'
        else:
            
            display_board(the_board)
            
            position = player_choice(the_board)
            
            board_marker(the_board, player2_marker, position)
            
            if win_condition(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has WON!!!')
                gameon = False
            else:
                if board_full(the_board):
                    display_board(the_board)
                    print('Game Tied!!!')
                    break
                else:
                    turn = 'Player 1'
            
                
    if not replay():
        print('Hope you had fun!!!')
        break

