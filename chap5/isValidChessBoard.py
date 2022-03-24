import fnmatch

def isValidChessBoard(board):
    wkingCount = 0
    bkingCount = 0
    wpawnCount = 0
    bpawnCount = 0
    bPattern = 'b*'
    wPattern = 'w*'
    bpiecesCount = 0
    wpiecesCount = 0
    verticalPosition = ('1', '2', '3', '4', '5', '6', '7', '8')
    horizontalPosition = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    allowedPositions = []
    allowedColors = ('w', 'b')
    allowedPieces = ('king', 'rook', 'bishop', 'queen', 'knight', 'pawn')
    allowedChessPieces = []

    for ii in range(len(allowedColors)):
        for kk in range(len(allowedPieces)):
            allowedChessPieces.insert(ii + kk, allowedColors[ii] + allowedPieces[kk])

    for ii in range(len(verticalPosition)):
        for kk in range(len(horizontalPosition)):
            allowedPositions.insert(ii + kk, verticalPosition[ii] + horizontalPosition[kk])

    for key, value in board.items():
        # Counts number of white kings
        if value == 'wking':
            wkingCount += 1
        # Counts number of black kings
        if value == 'bking':
            bkingCount += 1
        # Counts number of white pawns
        if value == 'wpawn':
            wpawnCount += 1
        # Counts number of black pawns
        if value == 'bpawn':
            bpawnCount += 1
        # Counts number of white pieces
        if (fnmatch.fnmatch(value, wPattern)):
            wpiecesCount += 1
        # Counts number of black pieces
        if (fnmatch.fnmatch(value, bPattern)):
            bpiecesCount += 1
        # Checks for invalid chess pieces
        if value not in allowedChessPieces:
            print('Error ' + value +' chess piece not allowed')
        # Checks for invalid position
        if key not in allowedPositions:
            print('Error: ' + key + ' position not allowed')

    if (wkingCount > 1):
        print('Error: ' + str(wkingCount) + ' white kings')
    if (bkingCount > 1):
        print('Error: ' + str(bkingCount) + ' black kings')
    if (wpawnCount > 8):
        print('Error: ' + str(wpawnCount) + ' white pawns')
    if (bpawnCount > 8):
        print('Error: ' + str(bpawnCount) + ' black pawns')
    if (wpiecesCount > 16):
        print('Error: ' + str(wpiecesCount) + ' white pieces, expected 16 max.')
    if (bpiecesCount > 16):
        print('Error: ' + str(bpiecesCount) + ' black pieces, expected 16 max.')

testBoard = {'1z': 'wking', '1b': 'wking', '1c' : 'w1', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', '2c' : 'w2', }

i