def printBoard(xState, oState):
    states = []
    for i in range(9):
        states.append('X' if xState[i] else 'O' if oState[i] else i)

    print(f"{states[0]} | {states[1]} | {states[2]}")
    print("--|---|--")
    print(f"{states[3]} | {states[4]} | {states[5]}")
    print("--|---|--")
    print(f"{states[6]} | {states[7]} | {states[8]}")

def checkWin(xState, oState):
    winningStates = [[0,1,2],
                    [3,4,5],
                    [6,7,8],
                    [0,3,6],
                    [1,4,7],
                    [2,5,8],
                    [0,4,8],
                    [2,4,6]
    ]

    for state in winningStates:
        xWins, oWins =  0,0
        for index in state:
            xWins += xState[index]
            oWins += oState[index]
        if xWins == 3:
            print("X won the match !")
            return 1
        elif oWins == 3:
            print("O won the match!")
            return 0
    else:
        return -1
        

if __name__=='__main__':
    xState = [0 for _ in range(9)]
    oState = xState.copy()

    turn = 1

    while(True):
        printBoard(xState, oState)
        if turn == 1:
            print("X's Turn")
            position = int(input("Position: "))
            xState[position] = 1 
        else:
            print("O's Turn")
            position = int(input("Position: "))
            oState[position] = 1 
        cWin = checkWin(xState, oState)
        if cWin != -1:
            print('Macth Over')
            break
        turn = 1 - turn

