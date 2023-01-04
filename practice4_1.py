import pyfiglet

count1 =0
count2 =0

title = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
print (title)

def show():
    for row in game_board:
        for call in row:
            print(call, end="")
        print()
def chek_game():
    if( game_board[0][0]=="X " and game_board[0][1]=="X " and game_board[0][2]=="X " or 
    game_board[1][0]=="X " and game_board[1][1]=="X " and game_board[1][2]=="X " or
    game_board[2][0]=="X " and game_board[2][1]=="X " and game_board[2][2]=="X " or
    game_board[2][0]=="X " and game_board[1][1]=="X " and game_board[0][2]=="X " or
    game_board[0][0]=="X " and game_board[1][1]=="X " and game_board[2][2]=="X "or
    game_board[0][0]=="X " and game_board[1][0]=="X " and game_board[2][0]=="X "or
    game_board[0][1]=="X " and game_board[1][1]=="X " and game_board[2][1]=="X "or
    game_board[0][2]=="X " and game_board[1][2]=="X " and game_board[2][2]=="X "):
        print("player1 wins")
        exit()
    if( game_board[0][0]=="O " and game_board[0][1]=="O " and game_board[0][2]=="O " or 
    game_board[1][0]=="O " and game_board[1][1]=="O " and game_board[1][2]=="O " or
    game_board[2][0]=="O " and game_board[2][1]=="O " and game_board[2][2]=="O " or
    game_board[2][0]=="O " and game_board[1][1]=="O " and game_board[0][2]=="O " or
    game_board[0][0]=="O " and game_board[1][1]=="O " and game_board[2][2]=="O "or
    game_board[0][0]=="O " and game_board[1][0]=="O " and game_board[2][0]=="O "or
    game_board[0][1]=="O " and game_board[1][1]=="O " and game_board[2][1]=="O "or
    game_board[0][2]=="O " and game_board[1][2]=="O " and game_board[2][2]=="O "):
        print("player2 wins")
        exit()


game_board=[["- ","- ","- "],
            ["- ","- ","- "],
            ["- ","- ","- "]] 
show()


while count1<6 and count2<5:

    print("player1")
    while True:
        row=int(input())
        col=int(input())
        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col]=="- ":
                game_board[row][col]="X "
                show()
                chek_game()
                break
            else:
        
                print("select another cell")
        else:
            print("enter row and col between 0 and2")

    print("player2")
    while True:
        row=int(input())
        col=int(input())
        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col]=="- ":
                game_board[row][col]="O "

                show()
                chek_game()
                break

            else:
                print("select another cell")
        else:
            print("enter row and col between 0 and 2")