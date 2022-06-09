import random
r=[]
for i in range(50):
    n=random.randint(10,560)
    r.append(n)

l=[[r[12],r[8],r[30]],[r[40],r[44],r[38]],[r[0],r[26],r[29]]]
l2=[[r[12],r[8],r[30]],[r[40],r[44],r[38]],[r[0],r[26],r[29]]]
l3=[[r[12],r[8],r[30]],[r[40],r[44],r[38]],[r[0],r[26],r[29]]]

ch=None

winner=None
def insert(ch,val):
    if ch%3==0 and ch<=9:
        ch2=int((ch/3)-1)
        l[ch2][2]=val
        l2[ch2][2] = val
    elif ch<=9 and ch%3==1:
        ch2=int(((ch+2)/3)-1)
        l[ch2][0]=val
        l2[ch2][0] = val
    elif ch<=9 and ch%3==2:
        ch2=int(((ch+1)/3)-1)
        l[ch2][1]=val
        l2[ch2][1] = val

end=False
ll=[1,2]
win_pl=None

def check():
    global end
    end = False
    if l[0][0] in ll and l[0][1] in ll and l[0][2] in ll and l[1][0] in ll and l[1][1] in ll and l[1][2] in ll and l[2][0] in ll and l[2][1] in ll and l[2][2] in ll:
        win_pl='Tie'
        end=True
    else:
        for i in range(3):
            if l[0][i]==l[1][i] and l[0][i]==l[2][i] and l[0][i] in ll:
                end=True
                winner=l[0][i]
                if winner==1:
                    win_pl='Player 1'
                elif winner==2:
                    win_pl='Player 2'
                else:
                    win_pl='No-one'
                end=True
            elif l[i][0]==l[i][1] and l[i][0]==l[i][2] and l[i][0] in ll:
                winner=l[i][0]
                if winner==1:
                    win_pl='Player 1'
                elif winner==2:
                    win_pl='Player 2'
                else:
                    win_pl='No-one'
                end=True
                end=True
            elif l[0][0]==l[1][1] and l[0][0]==l[2][2] and l[0][0] in ll:
                end=True
                winner=l[0][0]
                if winner==1:
                    win_pl='Player 1'
                elif winner==2:
                    win_pl='Player 2'
                else:
                    win_pl='No-one'
                end=True
            elif l[0][2]==l[1][1] and l[0][2]==l[2][0] and l[0][2] in ll:
                winner=l[0][2]
                if winner==1:
                    win_pl='Player 1'
                elif winner==2:
                    win_pl='Player 2'
                else:
                    win_pl='No-one'
                end=True
    try:
        print("=============")
        print("Winning Player: ",win_pl)
        print("=============")
    except:
        pass
    print("l",l)

def graphics():
    for i in l2[0]:
        if i==1:
            ind=l2[0].index(i)
            l3[0][ind]='''| O |'''
            l2[0][ind] = '''| O |'''
        elif i==2:
            ind=l2[0].index(i)
            l3[0][ind]='''| X |'''
            l2[0][ind] = '''| X |'''
        elif type(i) is not int:
            pass
        else:
            ind=l2[0].index(i)
            l3[0][ind]='''|  |'''

    for i in l2[1]:
        if i==1:
            ind=l2[1].index(i)
            l3[1][ind]='''| O |'''
            l2[1][ind] = '''| O |'''
        elif i==2:
            ind=l2[1].index(i)
            l3[1][ind]='''| X |'''
            l2[1][ind] = '''| X |'''

        elif type(i) is not int:
            pass
        else:
            ind=l2[1].index(i)
            l3[1][ind]='''|  |'''

    for i in l2[2]:
        if i==1:
            ind=l2[2].index(i)
            ind=l2[2].index(i)
            l3[2][ind]='''| O |'''
            l2[2][ind] = '''| O |'''
        elif i==2:
            ind=l2[2].index(i)
            ind=l2[2].index(i)
            l3[2][ind]='''| X |'''
            l2[2][ind] = '''| X |'''

        elif type(i) is not int:
            pass
        else:
            ind=l2[2].index(i)
            l3[2][ind]='''|  |'''
    print(f"{l3[0][0]}{l3[0][1]}{l3[0][2]}")
    print("-------------")
    print(f"{l3[1][0]}{l3[1][1]}{l3[1][2]}")
    print("-------------")
    print(f"{l3[2][0]}{l3[2][1]}{l3[2][2]}")
    print("-------------")
    print("L3: ",l3)
    print("L2: ",l2)


print("Welcome to Tic Tac Toe")
starting = '''   |   |   
-----------
   |   |   
-----------
   |   |   '''
print(starting)
while end==False:
    for i in range(2):
        if end==False:
            if i==0:
                print("Player 1 chance")
                ch = int(input("Enter: "))
                insert(ch,1)
                graphics()
                check()
            else:
                print("Player 2 chance")
                ch = int(input("Enter: "))
                insert(ch, 2)
                graphics()
                check()

def another():
    l = [[r[12], r[8], r[30]], [r[40], r[44], r[38]], [r[0], r[26], r[29]]]
    l2 = [[r[12], r[8], r[30]], [r[40], r[44], r[38]], [r[0], r[26], r[29]]]
    l3 = [[r[12], r[8], r[30]], [r[40], r[44], r[38]], [r[0], r[26], r[29]]]

    ch = None

    winner = None
    win_pl=None

    while end==False:
        for i in range(2):
            if end==False:
                if i==0:
                    print("Player 1 chance")
                    ch = int(input("Enter: "))
                    insert(ch,1)
                    graphics()
                    check()
                else:
                    print("Player 2 chance")
                    ch = int(input("Enter: "))
                    insert(ch, 2)
                    graphics()
                    check()


if end==True:
    ch2=input("Enter 'y' to play another game and 'n' to exit: ").lower()
    if ch2=='y':
        end=False
        another()
    elif ch2=='n':
        print("____________")
        print("Good-bye !")
        end=True
