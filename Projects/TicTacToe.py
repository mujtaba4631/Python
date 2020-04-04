#FUNCTION TO DISPLAY THE BOARD
def display_board(board):
    
    print('\n'*100)
    print(board[7]+ '  | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(board[4]+ '  | ' + board[5] +' | ' + board[6])
    print('---|---|---')
    print(board[1]+ '  | ' + board[2] +' | ' + board[3])



#TO TAKE INPUT FROM THE USER TO SELECT THE MARKER
def player_input():
    player1 = 'Z'
    while(player1 != 'X' and player1 != 'O' ):
        player1 = input("Enter the input for player1 ")
    if player1 == 'X':
        print('Player1 = X \nPlayer2 = O')
        return ('X','O')
    else:
        print('Player1 = O \nPlayer2 = X')
        return ('O','X')
    
#ADD THE MARKER TO THE LIST
def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)
    
#TO CHECK THE WIN CONDITION
def win_check(board, mark):
    if ((board[1] ==  board[2]==  board[3] == mark) or (board[1] ==  board[4]==  board[7] == mark)
       or (board[2] ==  board[5] == board[8] == mark) or (board[3] ==  board[6] ==  board[9] == mark)
       or (board[4] ==  board[5] == board[6] == mark) or (board[7] ==  board[8] ==  board[9] == mark)
       or (board[1] ==  board[5] == board[9] == mark) or (board[3] ==  board[5] ==  board[7] == mark)):
        return True
    else:
        return False

import random

#RANDOMLY SELECTING WHO WILL PLAY
def choose_first():
    r1 = random.randint(0,1)
    if (r1 == 1):
        return 'Player 1'
    else: 
        return 'Player 2'

#CHECK FOR EMPTY SPACE    
def space_check(board, position):
    if(board[position] == ' '):
        return True
    else:
        return False

#CHECK IF THE BOARD IS FULL
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#ENTER THE POSITION
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position): 
        position=int(input("Please enter the position between 1-9"))
        
    return position

#EXIT CONDITION
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
          
          #WIN CONDITION
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                #TIE GAME
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            #WIN CONDITION
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                #TIE GAME
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
   #EXIT CONDITION
    if not replay():
        break





