import random
import os.path
import json

all_move = [1,2,3,4,5,6,7,8,9]
possible_move = []
#grid for the game
def draw_board(board):
    for x in range(1,8):
        if(not x  % 2 == 0):
            for y in range(1,8):
                print("-",end=" ")
        else :
            for y in range(1,8):
                if(not y  % 2 == 0):
                    print("|",end=" ")
                else:
                    print(board[int(x / 2) - 1][int(y / 2) - 1],end=" ")
                    
        print(" ")
    pass
#welcome message and layout of game
def welcome(board):
    print("Welcome to the Unbeatable Noughts and Crosses game.")
    print("The board layout is show below:")
    draw_board(board)
    pass

def initialise_board(board):
    for x in range(0,3):
        for y in range (0,3):
            board[x][y] = " "
    # develop code to set all elements of the board to one space ' '
    return board
#for players input
def get_player_move(board):
    counter = 0
    possible_move.clear()
    for x in board:
        for num in x:
            if(counter > len(all_move)):
                break
            elif(num == " "):
                possible_move.append(all_move[counter])
            counter+=1
    print(possible_move)
    response = int(input("Choose your square : "))
    while (not (response in possible_move)):
        print("Please enter valid response")
        response = int(input("Choose your square : "))
    row = int((response -1)/3)
    col = (response - 1) % 3 
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    return row, col
#for computers move
def choose_computer_move(board):
    counter = 0
    possible_move.clear()
    for x in board:
        for num in x:
            if(counter > len(all_move)):
                break
            elif(num == " "):
                possible_move.append(all_move[counter])
            counter+=1
    if possible_move :
        response = random.choice(possible_move)
        row = int((response -1)/3)
        col = (response - 1) % 3
    else:
        return -1,-1
    return row, col

#to check player has won or computer
def check_for_win(board,mark):
    
    for x in range (0,3):
        if(board[x][x] != " " and board[x][0] == board[x][1] and board[x][2] == board[x][1] and board[x][0] == mark):
            if(mark == "X"):
                print("You Win")
            else:
                print("You Lose")
            return True
        elif(board[x][x] != " " and board[x][x] == board[1][x] and board[2][x] == board[1][x] and board[x][x] == mark):
            if(mark == "X"):
                print("You Win")
            else:
                print("You Lose")
            return True
    if(board[0][0] != " " and board[0][0] == board[1][1] and board[1][1] == board[2][2]and board[0][0] == mark ):
            if(mark == "X"):
                print("You Win")
            else:
                print("You Lose")
            return True
    elif(board[2][0] != " " and board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] == mark):
            if(mark == "X"):
                print("You Win")
            else:
                print("You Lose")
            return True
    

    return False
#to check if the game is draw
def check_for_draw(board):
    counter = 0
    possible_move.clear()
    for x in board:
        for num in x:
            if(counter > len(all_move)):
                break
            elif(num == " "):
                possible_move.append(all_move[counter])
            counter+=1
    if not possible_move:
        return True
    else:
        return False

#to play game(mechanism)
def play_game(board):
    space_board =  initialise_board(board)
    draw_board(space_board)
    isWin = False
    isDraw = False
    while not (isWin or isDraw):
        row , col = get_player_move(space_board)
        board[row][col] = "X"
        result_of_X = check_for_win(board,"X")
        if(result_of_X):
            draw_board(board)
            isWin = True
            return 1
        isDraw = check_for_draw(board)
        com_row,com_col = choose_computer_move(board)
        if(not(com_row == -1 and com_col == -1)):
            board[com_row][com_col] = "O"
            result_of_O = check_for_win(board,"O")
            if(result_of_O):
                draw_board(board)
                isWin = True
                return -1
        else:
            isDraw = check_for_draw(board)
        draw_board(board)
    
    if isDraw:
        return 0
    

#options
def menu():
    choice = input("""Enter one of the following options : \n1 - Play the game\n2 - Save your score in the leaderboard
3 - Load and display the leaderboard\nq - End the program\n1, 2, 3 or q? """)
    return choice
#to show score
def load_scores():
    if os.path.getsize('leaderboard.txt') != 0:
        file = open("leaderboard.txt","r")
        read = file.read()
        leaders = json.loads(read)
        file.close()
    else:
        leaders = {"Leader Board is":"empty"}
  
    return leaders
#save score in txt file (file handling)
def save_score(score):
    user_name = input("Enter User Name : ")
    if os.path.getsize('leaderboard.txt') != 0:
        file = open("leaderboard.txt","r+")
        read = file.read()
        dict_file = json.loads(read)
        file.seek(0)
        file.truncate()
        new_dict = {user_name:score}
        final_dict = {**dict_file,**new_dict}
        file.write(json.dumps(final_dict))
        file.close()
    else:
        file = open("leaderboard.txt","w")
        new_dict = {user_name:score}
        file.write(json.dumps(new_dict))
        file.close()

    return

#show leaderboard scores
def display_leaderboard(leaders):
    print(leaders)

    pass
from noughtandcrosses import *

def main():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    total_score = 0
    welcome(board)
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is :',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return
if __name__ == '__main__':
    main()

        