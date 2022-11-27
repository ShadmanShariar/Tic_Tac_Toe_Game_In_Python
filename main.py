# Author - Shadman Shariar
# Email - shadmanshariar007@gmail.com

while(True):
   print("Eneter your Sign X / O : ",end="")
   s = input()
   us = s[0]
   if (len(s) > 1):
      print("Enter a valid character X / O ")
      continue
   if (us != 'X' and us != 'O'):
      print("Enter a valid character X / O ")
      continue
   if (us == 'X'):
      pc = 'O'
   if (us == 'O'):
      pc = 'X'
   break

print()
board = [['1', ' | ', '2', ' | ', '3'],
         ['--', '--', '--', '--', '--'],
         ['4', ' | ', '5', ' | ', '6'],
         ['--', '--', '--', '--', '--'],
         ['7', ' | ', '8', ' | ', '9']]
while(True):
    for i in range (0,5,1):
        for j in range (0,5,1):
           print(board[i][j],end='')
        print()
    print()
    print("Enter your postion : ",end="")
    pos = input()
    upos = pos[0]
    c = 0;
    for i in range (0,5,1):
        for j in range (0,5,1):
            if(board[i][j]==(upos) and c==0):
                board[i][j] = us
                c=1
    ok = 0
    if(board[0][0]==board[0][2] and board[0][2]==board[0][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[2][0] == board[2][2] and board[2][2] == board[2][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[2][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[4][0] == board[4][2] and board[4][2] == board[4][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[4][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][0] == board[2][0] and board[2][0] == board[4][0]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][2] == board[2][2] and board[2][2] == board[4][2]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][2] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][4] == board[2][4] and board[2][4] == board[4][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][4] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][0] == board[2][2] and board[2][2] == board[4][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][4] == board[2][2] and board[2][2] == board[4][0]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][4] + " Win the match !!")
        ok = 1;
        break;

    cc = 0;
    for i in range (0,5,1):
        for j in range (0,5,1):
            if(board[i][j]!='--' and board[i][j]!=' | ' and cc ==0  and board[i][j]!=us
            and board[i][j]!=pc):
                board[i][j] = pc
                cc=1

    print()
    print("------------------------")
    print()
    if(ok==1):
        break
    ok = 0
    if(board[0][0]==board[0][2] and board[0][2]==board[0][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[2][0] == board[2][2] and board[2][2] == board[2][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[2][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[4][0] == board[4][2] and board[4][2] == board[4][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[4][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][0] == board[2][0] and board[2][0] == board[4][0]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][2] == board[2][2] and board[2][2] == board[4][2]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][2] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][4] == board[2][4] and board[2][4] == board[4][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][4] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][0] == board[2][2] and board[2][2] == board[4][4]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][0] + " Win the match !!")
        ok = 1;
        break;

    if (board[0][4] == board[2][2] and board[2][2] == board[4][0]):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                print(board[i][j], end='')
            print()
        print()

        print(board[0][4] + " Win the match !!")
        ok = 1;
        break;

    if(ok==1):
        break