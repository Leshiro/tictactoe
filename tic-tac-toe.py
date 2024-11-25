print("""
TIC-TAC-TOE
      
    [1][2][3]
    [4][5][6]
    [7][8][9]   
      
Enter a number between 1-9 to play your turn.
Enter "Q" to quit.""")

print("""
    [ ][ ][ ]
    [ ][ ][ ]
    [ ][ ][ ]
""")

while True:
    spots = {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0,
        "5" : 0,
        "6" : 0,
        "7" : 0,
        "8" : 0,
        "9" : 0
    }

    placeholders = {
        "1" : " ",
        "2" : " ",
        "3" : " ",
        "4" : " ",
        "5" : " ",
        "6" : " ",
        "7" : " ",
        "8" : " ",
        "9" : " "
    }

    turn = 1
    moves = 0

    while True:
        if turn == 1:  
            player1_move = input("Player X's Turn: ")
            try:
                player1_move = int(player1_move)
            except ValueError:
                if player1_move == "Q" or player1_move == "q":
                    print("")
                    exit()
                else:
                    print("""
    Please enter a number between 1-9.
                """)
                continue
            if not 1 <= player1_move <= 9:
                print("""
    Please enter a number between 1-9.
                """)
                continue
            if not spots[f"{player1_move}"] == 0:
                print(f"""
    Spot [{player1_move}] is already occupied. 
    Please choose an available spot.
                """)
                continue
            spots[f"{player1_move}"] = 1
            placeholders[f"{player1_move}"] = "X"
            moves = moves + 1
            turn = 2
            if spots["1"] == spots["2"] == spots["3"] == 1 or spots["4"] == spots["5"] == spots["6"] == 1 or spots["7"] == spots["8"] == spots["9"] == 1 or spots["1"] == spots["4"] == spots["7"] == 1 or spots["2"] == spots["5"] == spots["8"] == 1 or spots["3"] == spots["6"] == spots["9"] == 1 or spots["1"] == spots["5"] == spots["9"] == 1 or spots["3"] == spots["5"] == spots["7"] == 1:
                game_message = "Player X wins the game!"
                print(f"""
    [{placeholders["1"]}][{placeholders["2"]}][{placeholders["3"]}]
    [{placeholders["4"]}][{placeholders["5"]}][{placeholders["6"]}]    {game_message}
    [{placeholders["7"]}][{placeholders["8"]}][{placeholders["9"]}]
    """)
                again = input("""Enter any key to play again, or enter "Q" to quit: """)
                if again == "q" or again == "Q":
                    print("")
                    exit()
                print("""Starting new game...""")
                moves = 0
                print("""
    [ ][ ][ ]
    [ ][ ][ ]
    [ ][ ][ ]
                  """)
                break
            if moves == 9:
                game_message = "It's a draw!"
                print(f"""
    [{placeholders["1"]}][{placeholders["2"]}][{placeholders["3"]}]
    [{placeholders["4"]}][{placeholders["5"]}][{placeholders["6"]}]    {game_message}
    [{placeholders["7"]}][{placeholders["8"]}][{placeholders["9"]}]
    """)
                again = input("""Enter any key to play again, or enter "Q" to quit: """)
                if again == "q" or again == "Q":
                    print("")
                    exit()
                print("""Starting new game...""")
                moves = 0
                print("""
    [ ][ ][ ]
    [ ][ ][ ]
    [ ][ ][ ]
                  """)
                break
            else:
                print(f"""
    [{placeholders["1"]}][{placeholders["2"]}][{placeholders["3"]}]
    [{placeholders["4"]}][{placeholders["5"]}][{placeholders["6"]}]
    [{placeholders["7"]}][{placeholders["8"]}][{placeholders["9"]}]
    """)     
                continue

        if turn == 2:
            try:    
                player2_move = int(input("Player O's Turn: "))
            except ValueError:
                print("""
    Please enter a number between 1-9.
                """)
                continue
            if not 1 <= player2_move <= 9:
                print("""
    Please enter a number between 1-9.
                """)
                continue
            if not spots[f"{player2_move}"] == 0:
                print(f"""
    Spot [{player1_move}] is already occupied. 
    Please choose an available spot.
                """)
                continue
            spots[f"{player2_move}"] = 2
            placeholders[f"{player2_move}"] = "O"
            moves = moves + 1
            turn = 1
            if spots["1"] == spots["2"] == spots["3"] == 2 or spots["4"] == spots["5"] == spots["6"] == 2 or spots["7"] == spots["8"] == spots["9"] == 2 or spots["1"] == spots["4"] == spots["7"] == 2 or spots["2"] == spots["5"] == spots["8"] == 2 or spots["3"] == spots["6"] == spots["9"] == 2 or spots["1"] == spots["5"] == spots["9"] == 2 or spots["3"] == spots["5"] == spots["7"] == 2:
                game_message = "Player O wins the game!"
                print(f"""
    [{placeholders["1"]}][{placeholders["2"]}][{placeholders["3"]}]
    [{placeholders["4"]}][{placeholders["5"]}][{placeholders["6"]}]    {game_message}
    [{placeholders["7"]}][{placeholders["8"]}][{placeholders["9"]}]
    """)
                again = input("""Enter any key to play again, or enter "Q" to quit: """)
                if again == "q" or again == "Q":
                    print("")
                    exit()
                print("""Starting new game...""")
                moves = 0
                print("""
    [ ][ ][ ]
    [ ][ ][ ]
    [ ][ ][ ]
                  """)
                break
            else:
                print(f"""
    [{placeholders["1"]}][{placeholders["2"]}][{placeholders["3"]}]
    [{placeholders["4"]}][{placeholders["5"]}][{placeholders["6"]}]
    [{placeholders["7"]}][{placeholders["8"]}][{placeholders["9"]}]
    """)     
                continue        
