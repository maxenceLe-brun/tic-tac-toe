from ia import*
from time import*


def morpion(n=1):
  '''
  "n" means the number of human that plays, didn't tested for n=0, and bcs i didn't implement it already, calm down
  anyway, i've had enough of these non-sense that i made lmao
  have a good try to understand my chaos ^^
  AND YES, my code is in english AND french. I'll do it on purpose. And it's not making you want to kill me less.
  '''
  
    if n == 1:
        player = 1
    L = [[0,0,0] for a in range(3)]
    example = "   |   |   \n---|---|---\n   |   |   \n---|---|---\n   |   |   "
    result = list(example)
    tour = 1
    joueur = 0
    print(example)
    while 1:
        print("player " + str(joueur%2+1) + ", please select your place :")
        
        #Bot's turn
        if n == 1 and player == joueur%2:
            A = ia(L[0]+L[1]+L[2],"O")
            print(A)
        
        #human's turn (any human being yk what it means? EVEN PILE BOMBS SHOULD PLAY IT)
        else:
            a = input()
            A = list(a)
            number = [str(a) for a in range(10)]
            while len(A)!=2:
                print("only 2 characters please")
                sleep(2)
                print("player " + str(joueur%2+1) + ", please select your place :")
                a = input()
                A = list(a)
                if len(A) == 0:
                  print("HAVE MERCY")
                elif (A[0] and A[-1]) not in number:
                    print("NUMBERS!!!!!!!!")
                    A.append(None)
       
        #TESTING PART (yeee, lesgo)
        for b in range(len(A)):
            A[b] = int(A[b])
        if L[A[0]][A[1]] == 0:                        #tests if the placement is avalaible or not
            L[A[0]][A[1]] = (joueur)%2+1
            if (joueur+1)%2 == 0:                     #tests for the player
                result[(A[1])*24 + (A[0]*4)+1] = "O"
            else:
                result[(A[1])*24 + (A[0]*4)+1] = "X"
            exemple = ""
            for c in result:
                exemple += c
            print(exemple)
        else:                                         #if the place isn't avalaible, it will not cancel the loop, 
            sleep(0.1)                                #it'll make just like the last one didn't even existed
            print("wrong place")                      #a ratio in a nutshell
            joueur -= 1
            tour -= 1
        joueur += 1
        tour += 1
        
        #END PART
        if tour > 9:
            print("egalite")
            break                                                                       #BREAKING BONE
        if L[0][0] == L[1][1] == L[2][2] != 0 or L[0][2] == L[1][1] == L[2][0] != 0:
            print("player "+str(joueur%2+1)+" has lost the game!")
            break
        B = 0
        for d in range(3):
            if L[d][0] == L[d][1] == L[d][2] != 0 or L[0][d] == L[1][d] == L[2][d] != 0:
                B = 1
                print("player " + str(joueur%2+1) + " has lost the game!")
        
        #For those who don't know, "if 1:" is like "if True:", and 0 is False (obviously), so it's much more simple to do it that way
        if B:break
