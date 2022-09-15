import random
import copy

print("Welcome to Tic-Tac-Toe!")
print("The board is enumerate like this:")

board_matrix = [[j+(i*3)+1 for j in range(3)] for i in range(3)]    #Values witch will show on screen
board_values = [[int(0) for j in range(3)] for i in range(3)]       #Values witch let us know the position of the moves
start_game = True                                                   
selection = 0 
position_avaible = [1,2,3,4,5,6,7,8,9]

def clear_game():
    #Reset the board and prepear its to a new game
    global board_matrix
    board_matrix = [[j+(i*3)+1 for j in range(3)] for i in range(3)]
    global board_values
    board_values = [[int(0) for j in range(3)] for i in range(3)]
    global start_game
    start_game = True
    global position_avaible
    position_avaible = [1,2,3,4,5,6,7,8,9]

def show_board():
    #Displya the board on screen
    for i in range(3):
        print(f'{board_matrix[i][0] if board_matrix[i][0] else " "} | {board_matrix[i][1] if board_matrix[i][1] else " "} | {board_matrix[i][2] if board_matrix[i][2] else " "}')
    print("")

def take(num, play):
    #Make a move and set the rigth value into the board_values
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
            
def best_choise():
    #This function select the best move to make acording to the current board.
    position = check_x_victory()
        
    if start_game == True:
        return random.choice(position_avaible) #When the game start, choice a random position
    else:
        best = [0,0,0] #Index:value -> 0:save the lowest sum / 1: save the row number / 2: save the column number
        
        for n in range(len(position_avaible)): 
            #iterate between avaible position, and check witch is the best one.    
            for i in range(3):
                for j in range(3):                    
                    
                    if position_avaible[n] == board_matrix[i][j]:
                        board_values_aux = copy.deepcopy(board_values) 
                        board_values_aux[i][j] = int(-1)

                        for k in range(3):
                            sum_ve = sum_v(k, board_values_aux)
                            if sum_ve < best[0]:
                                best[0] = sum_ve
                                best[1], best[2] = i, j

                            sum_ho = sum_h(k, board_values_aux)
                            if sum_ho < best[0]:
                                best[0] = sum_ho
                                best[1], best[2] = i, j

                            sum_d1 = sum_d(1, board_values_aux)
                            if sum_d1 < best[0]:
                                best[0] = sum_d1
                                best[1], best[2] = i, j

                            sum_d2 = sum_d(-1, board_values_aux)
                            if sum_d2 < best[0]:
                                best[0] = sum_d2
                                best[1], best[2] = i, j
        
        if best[0] == -3 or position == False: #Check if the best choice it's a win move or if the oponent can't win on his next move.    
            return board_matrix[best[1]][best[2]]
        else:
            return board_matrix[position[0]][position[1]] #If the oponent can win on his next move, then take that position
        
def check_x_victory():
    #Check if the oponent can win on his nex move.
    
    #Count the number of X's in one horizontal line
    for i in range(3):
        count_ones = 0
        position = 0
        for j in range(3):
            if board_values[i][j] == 1:
                count_ones += 1
            elif board_values[i][j] == 0:
                position = j
            elif board_matrix[i][j] == "O":
                count_ones = 0
                break
        
        #If there is 2 X's then the oponent can win the game
        if count_ones == 2:
            print(f"X can win! H ({i, position})" )
            return [i, position]
    
    #Count the number of X's in one vertical line    
    for j in range(3):
        count_ones = 0
        position = 0
        for i in range(3):
            if board_values[i][j] == 1:
                count_ones += 1
            elif board_values[i][j] == 0:
                position = i
            elif board_matrix[i][j] == "O":
                count_ones = 0
                break
        
        #If there is 2 X's then the oponent can win the game
        if count_ones == 2:
            print(f"X can win! V ({position, j})" )
            return [position, j] 
    

    count_ones1 = 0
    position1 = [0,0]
    count_ones2 = 0
    position2 = [0,0]
    
    #Count the number of X's in direct diagonal line
    for j in range(3):
        if board_values[j][j] == 1:
            count_ones1 += 1
        elif board_values[j][j] == 0:
            position1 = [j, j]
        elif board_matrix[j][j] == "O":
            count_ones1 = 0
            break
    
    #Count the number of X's in revert diagonal line    
    for j in range(3):
        if board_values[j][2-j] == 1:
            count_ones2 += 1
        elif board_values[j][2-j] == 0:
            position2 = [j, 2-j]
        elif board_matrix[j][2-j] == "O":
            count_ones2 = 0
            break
    
    #If there is 2 X's then the oponent can win the game    
    if count_ones1 == 2:
        print(f"X can win! D1 ({position1})" )
        return position1  
    
    #If there is 2 X's then the oponent can win the game
    if count_ones2 == 2:
        print(f"X can win! D2 ({position2})" )
        return position2  
    
    return False

def sum_v(col,values):
    #Sum values in vertical lines
    sum_ve = 0
    
    for i in range(3):
        sum_ve += values[i][col]
    
    return sum_ve

def sum_h(row, values):
    #Sum values in horizontal lines
    sum_ho = 0
    
    for i in range(3):
        sum_ho += values[row][i]  
        
    return sum_ho

def sum_d(dia, values):
    #Sum values in diagonal lines
    sum_di = 0
        
    if dia == 1:
        for i in range(3):
            sum_di += values[i][i * dia]
    elif dia == -1:
        for i in range(3):
            sum_di += values[i][(2-i)]
    
    return sum_di

def check(num):
    #Verify if the input is an avaible number of the board
    if num not in position_avaible:
        return True
    else:
        return False
    
def there_is_winner():
    #check if there is a winner
    for i in range(3):
        sum_ve = sum_v(i, board_values)
        if abs(sum_ve) == 3:
            return sum_ve
        
        sum_ho = sum_h(i, board_values)
        if abs(sum_ho) == 3:
            return sum_ho

    sum_di1 = sum_d(1, board_values)
    if abs(sum_di1) == 3:
        return sum_di1
    
    sum_di2 = sum_d(-1, board_values)
    if abs(sum_di2) == 3:
        return sum_di2
    
win = False

def playerVsPc():
    #Function to Human vs PC 
    print("\n", "I'm first! I play with O's, you play with  X's.")
    
    while not win:        
        global start_game
        start_game = False
        finished_game = False  
        
        while not finished_game:
            take(best_choise(), "O")
            show_board()
            
            if there_is_winner() == -3:
                print("I WIN!")
                finished_game = True
                
            
            if len(position_avaible) == 0:
                print("It's a tie!")
                finished_game = True
                
            if not finished_game:
                player_choice = int(input("Your turn:"))
                
                while check(player_choice):
                    player_choice = int(input("Choice an avaible number of the board:"))
                
                take(player_choice, "X")
                show_board()
                
                if there_is_winner() == 3:
                    print("You WIN!")
                    finished_game = True
        
        while finished_game:
            choise = input("Do you want to play again? (S/N)\n")
                        
            if choise == "S":
                clear_game()                    
                show_board()
                select()
                finished_game = False
            elif choise == "N":
                exit()
            else: 
                print("You must to choise between S or N", end="\n")    

def playerVsPlayer():
    #Function to Human vs Human
    
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

def select():
    global selection
    while  selection == 0:
        selection = int(input(""))
        
        if selection == 1:
            playerVsPlayer()
        elif selection == 2:
            playerVsPc()
        else:
            print("You can chose only 1 or 2.")
            selection = 0  
            
clear_game()    
show_board()
print("How you want to play?","", "1)- Player 1 vs Player 2", "2)- Player 1 vs PC", sep="\n", end="\n")
select()