from random import*
def ia(board,signe):
    '''
    i fked up this part, as the bonus asked for a table that is :
        [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]
    but actually, it's more like:
        [[1, 4, 7], 
         [2, 5, 8], 
         [3, 6, 9]]
    dunno how i reversed the list... still work tho, but i mind changing this
    
    update from nowhere : the bug is not from here, but from the original file, that put L[0] as [1,4,7] but dunno why
    gonna try to repair this
    '''
    
    #selection of the player, but not really important (maybe a little)
    if signe == "X":
        player = 1
        enemy = 2
    elif signe == "O":
        player = 2
        enemy = 1
    
    else:print("FU") #i had a menta breakdown, don't mind it
    board2 = board[:]
    place = []
    [place.append([a, board[a]]) for a in range(len(board))]
    for b in range(len(board)):
        if board2[b] == 0:
            board2[b] = player
            L = [board2[0:3], board2[3:6], board2[6:9]]
            B = 0
            for d in range(3):
                if L[d][0] == L[d][1] == L[d][2] != 0 or L[0][d] == L[1][d] == L[2][d] != 0:
                    B = 1
            if B:
                return [b//3,b%3]
            elif L[0][0] == L[1][1] == L[2][2] != 0 or L[0][2] == L[1][1] == L[2][0] != 0:
                return [b//3,b%3]
        board2 = board[:]
    for b in range(len(board)):
        if board2[b] == 0:
            board2[b] = player
            board3 = board2[:]
            L = [board2[0:3], board2[3:6], board2[6:9]]
            B = 0
            for d in range(3):
                if L[d][0] == L[d][1] == L[d][2] != 0 or L[0][d] == L[1][d] == L[2][d] != 0:
                    B = 1
            if B:
                return [b//3,b%3]
            elif L[0][0] == L[1][1] == L[2][2] != 0 or L[0][2] == L[1][1] == L[2][0] != 0:
                return [b//3,b%3]
            else:
                for c in range(len(board)):
                    if board3[c] == 0:
                        board3[c] = enemy
                        l = [board3[0:3],board3[3:6],board3[6:9]]
                        B = 0
                        for d in range(3):
                            if l[d][0] == l[d][1] == l[d][2] != 0 or l[0][d] == l[1][d] == l[2][d] != 0:
                                B = 1
                        if B:
                            return [c//3,c%3]
                        elif l[0][0] == l[1][1] == l[2][2] != 0 or l[0][2] == l[1][1] == l[2][0] != 0:
                            return [c//3,c%3]
                    board3 = board2[:]
            board2 = board[:]
    listing = []
    for a in range(len(board)):
        if board[a] == 0:
            listing.append(a)
            print(listing)
    z = choice(listing)
    print(z+1)
    return [z//3,z%3]

def ia0(board,signe):
    '''
    the siplest difficulty, it plays at random places
    goodluck to play against this XD
    '''
    listing = []
    for a in range(len(board)):
        if board[a] == 0:
            listing.append(a)
            print(listing)
    z = choice(listing)
    print(z+1)
    return [z//3,z%3]
def ia1(board,signe):
    '''
    easy clutch
    '''
    ia(board,signe)
def ia2(board,signe):
    
    pass
