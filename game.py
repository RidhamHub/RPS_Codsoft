#  Design a user-friendly interface with clear instructions and feedback.
# at any cost code should not be stop..okok

import random

choices = {1:'Rock' , 2:'Paper' , 3:'scissors'}
cc = ['1','2','3']

print("\n............Please play carefully if you enter any wrong input then point will given to computer............\n")

while True:
    try :
        x = input("Press 1 : If you want to play till you want \npress 2 : If you want to play untill you or computer reaches your target\npress 3 : play for n times\n")
        if x not in (cc):
            print("Enter correct input : ")
            continue   
        break   
    except ValueError:
        print(f"value erroe : {ValueError} , please etner correct input")



if x == '1':
    retry = 'Y'
    pl_point = 0
    cp_point = 0

    while retry.upper() == 'Y':
        while True:
            try:
                pl_choise = input("Enter your choice...\nPress 1 : Rock\nPress 2 : Paper\nPress 3 : Scissors\n")
                if pl_choise not in (cc):
                    print("Please enter correct input---> 1 or 2 or 3")
                    continue
                break
            except ValueError:
                print(f"Value Error : {ValueError} ,please etner correct input")
                
        cp_choise = random.choice(cc)

        if pl_choise == cp_choise:
            print(
                f"\nYou both choose : {pl_choise}-->{choices[int(pl_choise)]}\n")
            print("It's a Tie!!")
            print(f"Your Point : {pl_point}\nComputer Point : {cp_point}\n")
        elif (pl_choise == '1' and cp_choise == '3') or \
            (pl_choise == '2' and cp_choise == '1') or \
                (pl_choise == '3' and cp_choise == '2'):
            print(
                f"\nPlayer choose : {pl_choise}-->{choices[int(pl_choise)]}\nComputer Choose : {cp_choise}-->{choices[int(cp_choise)]}")    
            print("You WIN...!!")
            pl_point += 1
            print(f"Your Point : {pl_point}\nComputer Point : {cp_point}\n")
        else:
            if cp_choise in ['1', '2', '3']:
                print(
                    f"\nPlayer choose : {pl_choise}-->{choices[int(pl_choise)]}\nComputer Choose : {cp_choise}-->{choices[int(cp_choise)]}")
            else:
                print("You have entered wrong input......")
            print("COMPUTER WIN..")
            cp_point += 1
            print(f"Your Point : {pl_point}\nComputer Point : {cp_point}\n")

        retry = input("ENter 'Y' or 'y' for play again or else enter any key to END the game : ")

    if pl_point > cp_point:
        print(
            f"You win the game with margin of : {pl_point-cp_point} point \n")
    elif cp_point > pl_point:
        print(
            f"Computer win the game with margin of : {cp_point-pl_point} point\n")
    else:
        print(
            f"You both have same {pl_point} points , SO no one is the winner...")
        
    print("...........................................Thank You for playing woth us.........................................")

        

if x == '2' :
    while True:
        try :
            p = int(input("Enter the score you want to do : "))
            if p not in range(1,10000):
                print("ENter correct input between 1 to 10000")
                continue
            break
        except ValueError :
                print(f"Value Error : {ValueError} , please etner correct input")
    ok = 0
    print(f"Ok then one will socore {p} firstly...will be winner \n")
    
    target = 0
    pl_point = 0
    cp_point = 0
    
    while target < p :
        while True:
            try:
                pl_choise = input("Enter your choice...\nPress 1 : Rock\nPress 2 : Paper\nPress 3 : Scissors\n")
                if pl_choise not in (cc):
                    print("Please enter correct input---> 1 or 2 or 3")
                    continue
                break
            except ValueError:
                print(f"Value Error : {ValueError} , please etner correct input")
                
            
        cp_choise = random.choice(cc)
        
        if pl_choise == cp_choise :
            print(f"\nYou both choose : {pl_choise}-->{choices[int(pl_choise)]}\n")
            print("It's a Tie!!")
            print(f"Your Point : {pl_point}\nComputer Point : {cp_point}\n")
        elif(pl_choise == '1' and cp_choise == '3') or \
            (pl_choise == '2' and cp_choise == '1') or \
            (pl_choise == '3' and cp_choise == '2') :
            # if pl_point == p-1 and cp_point == pl_point :
            #     print("............Hey user   It is 'Do or Die round so select carefully !!!        ...............' ")
            print(f"\nPlayer choose : {pl_choise}-->{choices[int(pl_choise)]}\nComputer Choose : {cp_choise}-->{choices[int(cp_choise)]}")
            print("You WIN...!!")
            pl_point += 1
            print(f"Your Point : {pl_point}\nComputer Point : {cp_point}\n")
        else :
            if cp_choise in ['1','2','3']:
                print(f"\nPlayer choose : {pl_choise}-->{choices[int(pl_choise)]}\nComputer Choose : {cp_choise}-->{choices[int(cp_choise)]}")
            else :
                print("You have entered wrong input......")
            print("COMPUTER WIN..")
            cp_point += 1
            print(f"Your Point : {pl_point}\nComputer Point : {cp_point}\n")
            
        target = max(pl_point,cp_point)
    
    if pl_point > cp_point :
        print(f"You win the game with margin of : {pl_point-cp_point} point \n")
    else :
        print(f"Computer win the game with margin of : {cp_point-pl_point} point\n")
        
    print("...........................................Thank You for playing woth us.........................................")

    
elif x == '3' :
    while True:
        try :
            n = int(input("Enter number of times you want to play : "))
            if n not in range(1,10000):
                print("ENter correct input between 1 to 10000")
                continue
            break
        except ValueError:
            print(f"Value erroe : {ValueError} , Please enter correct input")
            
            
    pl_point = 0
    cp_point = 0
    for _ in range(n):
        while True:
                try:
                    pl_choise = input("Enter your choice...\nPress 1 : Rock\nPress 2 : Paper\nPress 3 : Scissors\n")
                    if pl_choise not in (cc):
                        print("Please enter correct input---> 1 or 2 or 3")
                        continue
                    break
                except ValueError:
                    print(f"Value Error : {ValueError} , please etner correct input")
            
        cp_choise = random.choice(cc)

        if pl_choise == cp_choise :
                print(f"\nYou both choose : {pl_choise}-->{choices[int(pl_choise)]}\n")
                print("It's a Tie!!")
                print(f"Your Point : {pl_point}\nComputer Point : {cp_point}\n")
        elif(pl_choise == '1' and cp_choise == '3') or \
                (pl_choise == '2' and cp_choise == '1') or \
                (pl_choise == '3' and cp_choise == '2') :
                # if abs(pl_point-cp_point) == 1 and (n-(_+1)) == 0:
                #     print("............Hey user   It is 'Do or Die round so select carefully !!!        ...............' ")
                print(f"\nPlayer choose : {pl_choise}-->{choices[int(pl_choise)]}\nComputer Choose : {cp_choise}-->{choices[int(cp_choise)]}")
                print("You WIN...!!")
                pl_point += 1
                print(f"Your Point : {pl_point}\nComputer Point : {cp_point}\n")
        else :
                if cp_choise in ['1','2','3']:
                    print(f"\nPlayer choose : {pl_choise}-->{choices[int(pl_choise)]}\nComputer Choose : {cp_choise}-->{choices[int(cp_choise)]}")
                else :
                    print("You have entered wrong input......")
                print("COMPUTER WIN..")
                cp_point += 1
                print(f"Your Point : {pl_point}\nComputer Point : {cp_point}\n")
                
        
        print(f"Remaining round.....{n-(_+1)}\n")
    if pl_point > cp_point:
        print(f"You win the game with margin of : {pl_point-cp_point} point \n")
    elif cp_point > pl_point:
        print(f"Computer win the game with margin of : {cp_point-pl_point} point\n")
    else:
        print(f"You both have same {pl_point} points , SO no one is the winner...")
        
    print("...........................................Thank You for playing woth us.........................................")
    

else :
    print("You have entered wrong input...okok")
    
    
