def solveQueens(n):
    col = set()
    posDiag = set() # (row + colum) is a constant value throughout
    negDiag = set() # (row - colum) is a constant value throughout

    res = []
    board = [['_']*n for _ in range(n)] 

    def backtrack(row):
        if row == n:
            copy = [' '.join(row) for row in board]
            res.append(copy)
            return
        
        for column in range(n):
            if column in col or (row+column) in posDiag or (row-column) in negDiag:
                continue

            col.add(column)
            posDiag.add(row+column)
            negDiag.add(row-column)
            board[row][column] = 'Q'

            backtrack(row+1) # we go row wise recursive backtrack 
            
            col.remove(column)
            posDiag.remove(row+column)
            negDiag.remove(row-column)
            board[row][column] = '_'
    backtrack(0)
    return res 


result = solveQueens(int(input('No. of Queens: ')))

for soln in result:
    for row in soln:
        print(row)
    print()