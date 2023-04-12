def check_value(value):
    if value in used_number:
        print("Number already used,Enter another")
        return -1
    else:
        used_number.append(value)
        print("used number list::::::::", used_number)
        return value

def sum(a,b,c):
    return a+b+c
def check_win(xState,zState):
    wining_patterns = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wining_patterns:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]]) == 3):
            print("X won::::::::::::")
            return 1
        elif(sum(zState[win[0]],zState[win[1]],zState[win[2]]) == 3):
            print("O won:::::::::::::")
            return 0
    return -1
def printBoard(xState,zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0 )
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)


    print(f"{zero} |{one} |{two} ")
    print("--|--|--")
    print(f"{three} |{four} |{five} ")
    print("--|--|--")
    print(f"{six} |{seven} |{eight}")

xState = [0,0,0,0,0,0,0,0,0]
zState = [0,0,0,0,0,0,0,0,0]
used_number = []
turn = 1
while (True):
    printBoard(xState,zState)
    if turn == 1:
        print("X's chance")
        while (True):
            value = input("enter X's Position value (0-8) = ")
            if value.isdigit():
                int_val = int(value)
                if (int_val >= 0) and (int_val < 9):
                    print("integer value entered :::::", int_val)
                    final_value = check_value(int_val)
                    if (final_value != -1):
                        print("final value:::::::",final_value)
                        xState[final_value] = 1
                        turn = 1 - turn
                        break
                else:
                    print("Please enter within the mentioned range.")
            else:
                print("Invalid Integer,Please enter valid Number")

    else:
        print("O's Chance")
        while (True):
            value = input("enter O's Position value (0-8) = ")
            if value.isdigit():
                int_val = int(value)
                if (int_val >=0) and (int_val <9):
                    print("integer value entered :::::",int_val)
                    final_value = check_value(int_val)
                    if (final_value != -1):
                        print("Final value:::::",final_value)
                        zState[final_value] = 1
                        turn = 1 + turn
                        break
                else:
                    print("Please enter within the mentioned range.")
            else:
                print("Invalid Integer,Please enter valid Number")


    cwin = check_win(xState,zState)
    if (cwin != -1):
        print("Final result")
        printBoard(xState, zState)
        break