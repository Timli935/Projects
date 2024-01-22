#Initializing the grid
n = 3
grid = [["*" for i in range(n)] for j in range(n)] #creates the grid
turn = 0
#updating the grid
while turn < 10: #max number of turns, errors will not count
    if turn % 2 == 0:
        player = "X"
        current_move = input("Player " + player + ", please enter your move:")#prompting the user
        if current_move == "I win!":
            print("good job")
            break
        coords = current_move.split()
        a = int(coords[1])
        b = int(coords[1])
        if grid[a][b] != "*": # checking validity of the move
            continue
        else:
            turn += 1 # adding turns
            for i in range(n):
                for j in range(n):
                    if i == a and j == b: # change the grid according to input
                        grid[i][j] = "X"
                    print(grid[i][j], end = " ")
                print("\n")
    else:
        player = "O"
        current_move = input("Player " + player + ", please enter your move:")
        if current_move == "I win!":
            print("good job")
            break
        coords = current_move.split()
        a = int(coords[1])
        b = int(coords[1])
        if grid[a][b] != "*":
            continue
        else: 
            turn += 1
            for i in range(n):
                for j in range(n):
                    if i == a and j == b:
                        grid[i][j] = "O"
                    print(grid[i][j], end = " ")
                print("\n")
