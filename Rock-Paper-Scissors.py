def rpsgame():
    """returns winner message based on choices"""
    run = True
    count = 0
    while(run == True):
        var = ""
        choice1 = ""
        choice2 = ""
        choice1 = raw_input("Choose RPS: ")
        choice2 = raw_input("Choose RPS: ")
        if choice1 == choice2:
            var = "Tie!"
        elif choice1 == 'rock':
            if choice2 == 'scissors':
                var = "Rock wins!"
            elif choice2 == 'paper':
                var = "Paper wins!"
        elif choice1 == 'paper':
            if choice2 == 'scissors':
                var = "Scissors wins!"
            elif choice2 == 'rock':
                var = "Paper wins!"
        elif choice1 == 'scissors':
            if choice2 == 'rock':
                var = "Rock wins!"
            elif choice2 == 'paper':
                var = "Scissors wins!"
        print(var)
        count = count + 1
        if(count >= 3):
            run = False


def rpsgame2():
    """returns winner message based on choices"""
    choice1 = raw_input("Choose RPS: ")
    choice2 = raw_input("Choose RPS: ")
    if choice1 == choice2:
        var = "Tie!"
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            var = "Rock wins!"
        elif choice2 == 'paper':
            var = "Paper wins!"
    elif choice1 == 'paper':
        if choice2 == 'scissors':
            var = "Scissors wins!"
        elif choice2 == 'rock':
            var = "Paper wins!"
    elif choice1 == 'scissors':
        if choice2 == 'rock':
            var = "Rock wins!"
        elif choice2 == 'paper':
            var = "Scissors wins!"
rounds = int(raw_input("Enter number of rounds: "))
player1_name = raw_input("Enter player1 name: ")
player2_name = raw_input("Enter player2 name: ")
counter = 0
while counter != rounds:
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
    counter += 1
print("{} and {} thanks for playing!".format(player1_name, player2_name))
