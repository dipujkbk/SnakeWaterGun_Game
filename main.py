import random
# Snake Water Gun or Rock Paper Scissors
def game(comp,you):
    if comp == you:
        return None
    if(comp=='s'):
        if(you=='w'):
            return False
        else:
            return True
    elif comp=='w':
        if(you=='s'):
            return True
        else:
            return False
    else:
        if(you=='s'):
            return False
        else:
            return True


var = 'y'
while var=='y':
    print("Computer's Turn: Snake(s) or  Water(w) or Gun(g)")
    randNo = random.randint(1,3)
    if randNo == 1:
        comp= 's'
    elif randNo == 2:
        comp = 'w'
    if randNo == 3:
        comp = 'g'
    you = input("Your's Turn: Snake(s) or  Water(w) or Gun(g)? ")
    a = game(comp,you)

    print(f"Computer choose {comp} ")
    print(f"You choose {you} ")
    if a == None:
        print("The game is a Tie! ")
    elif a:
        print("You Win :-)")
    else:
        print("You loose :-(")
    var = input('Do you want to play the game(enter y) or you want to exit(enter any charcter)? ')

