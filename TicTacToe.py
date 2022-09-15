import random

print("Welcome to Tic-Tac-Toe!")
print("The board is enumerate like this:")

board_matrix = [[j+(i*3)+1 for j in range(3)] for i in range(3)]
board_values = [[int(0) for j in range(3)] for i in range(3)]
def show_board():
    for i in range(3):
        print(f'{board_matrix[i][0]} | {board_matrix[i][1]} | {board_matrix[i][2]}')
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
                position_taked.append(num)
                
                if play == "O":
                    board_values[i][j] = int(-1)
                else:
                    board_values[i][j] = int(1)
                
                break
            

def check(num):
    if num not in position_avaible:
        return True
    else:
        return False
    
def there_is_winner():
    sum_v = [0,0,0]
    sum_d = [0,0]
    
    
    for i in range(3):
        sum_d[0] += board_values[i][i]
        sum_d[1] += board_values[-i][-i]
        
        for j in range(3):
            sum_v[i] += board_values[j][i]
                    
        if abs(sum_v[i]) == 3:
            return sum_v[i]
            
        if abs(sum(board_values[i])) == 3:
            return sum(board_values[i])

        if abs(sum_d[0]) == 3:
            return sum_d[0]
        
        if abs(sum_d[1]) == 3:
            return sum_d[1]    
    
win = False

def playerVsPc():
    print("\n", "I'm first! I play with O's, you play with  X's.")
    
    while not win:
        
        take(random.choice(position_avaible), "O")
        show_board()
        
        if there_is_winner() == -3:
            print("I WIN!")
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