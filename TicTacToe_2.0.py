import random
import copy

print("Welcome to Tic-Tac-Toe!")
print("The board is enumerate like this:")

board_matrix = [[j+(i*3)+1 for j in range(3)] for i in range(3)]
board_values = [[int(0) for j in range(3)] for i in range(3)]
start_game = True

def show_board():
    for i in range(3):
        print(f'{board_matrix[i][0] if board_matrix[i][0] else " "} | {board_matrix[i][1] if board_matrix[i][1] else " "} | {board_matrix[i][2] if board_matrix[i][2] else " "}')
    print("")
    
show_board()

print("How you want to play?","", "1)- Player 1 vs Player 2", "2)- Player 1 vs PC", sep="\n", end="\n")

selection = 0       
position_avaible = [1,2,3,4,5,6,7,8,9]
position_taked = []

def take(num, play):
    for i in range(3):
        for j in range(3):
            if num == board_matrix[i][j]:
                board_matrix[i][j] = play
                del position_avaible[position_avaible.index(num)]
                
                if play == "O":
                    board_values[i][j] = int(-1)
                else:
                    board_values[i][j] = int(1)
                
                break
            
def bestChoise():
    best = [0, 0, 0]
    
    for num in position_avaible:
        board_values_aux = copy.deepcopy(board_values)
        for i in range(3):    
            for j in range(3):
                if num == board_matrix[i][j]:
                    board_values_aux[i][j] = int(-1)
                            
                    for k in range(3):            
                        if sum_v(k, board_values_aux) < best[0]:
                            best[0] = sum_v(k, board_values_aux)
                            best[1], best[2] = i,j
                                                    
                    for k in range(3):
                        if sum_h(k, board_values_aux) < best[0]:
                            best[0] = sum_h(k, board_values_aux)
                            best[1], best[2] = i,j
                            
                    if sum_d(1, board_values_aux) < best[0]:
                        best[0] = sum_d(1, board_values_aux)
                        best[1], best[2] = i,j
                    elif sum_d(-1, board_values_aux) - 1 < best[0]:
                        best[0] = sum_d(-1, board_values_aux)
                        best[1], best[2] = i,j
                    
                
    print(board_matrix[best[1]][best[2]])
    print(start_game)
    if start_game:
        return random.choice(position_avaible)
    else:
        return board_matrix[best[1]][best[2]]
    
def sum_v(col,values):
    sumV = 0
    
    for i in range(3):
        sumV += values[i][col]
    
    return sumV

def sum_h(row, values):
    sumH = 0
    
    for i in range(3):
        sumH += values[row][i]
        
    return sumH

def sum_d(dia, values):
    sumD = 0
    
    for i in range(3):
        if dia == 1:
            sumD += values[i][i * dia]
        elif dia == -1:
            sumD += values[i][(i + 1) * dia]
    
    return sumD

def check(num):
    if num not in position_avaible:
        return True
    else:
        return False
    
def there_is_winner():
    for i in range(3):
        sumV = sum_v(i, board_values)
        if abs(sumV) == 3:
            return sumV
        
        sumH = sum_h(i, board_values)
        if abs(sumH) == 3:
            return sumH

    dia1 = sum_d(1, board_values)
    if abs(dia1) == 3:
        return dia1
    
    dia2 = sum_d(-1, board_values)
    if abs(dia2) == 3:
        return dia2
    
win = False

def playerVsPc():
    print("\n", "I'm first! I play with O's, you play with  X's.")
    
    while not win:
        
        take(bestChoise(), "O")
        show_board()
        global start_game
        start_game = False
        
        if there_is_winner() == -3:
            print("I WIN!")
            print(board_values)
            break
        
        player_choice = int(input("Your turn:"))
        
        while check(player_choice):
            player_choice = int(input("Choice an avaible number of the board:"))
        
        take(player_choice, "X")
        show_board()
        
        if there_is_winner() == 3:
            print("You WIN!")
            break

def playerVsPlayer():
    player = "O"
    while not win:
        player_choice = int(input(f"{player}'s turn:"))
        
        while check(player_choice):
            player_choice = int(input("Choice an avaible number of the board:"))
            
        take(player_choice, player)       
        show_board()
        
        if there_is_winner() == -3:
            print("Player with O WIN!")
            break
        elif there_is_winner() == 3:
            print("Player with X WIN!")
            break
        
        if player == "O":
            player = "X"
        else:
            player = "O"

while selection == 0:
    selection = int(input(""))
    
    if selection == 1:
        playerVsPlayer()
    elif selection == 2:
        playerVsPc()
    else:
        print("You can chose only 1 or 2.")
        selection = 0