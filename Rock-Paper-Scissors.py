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
counter = 0
while counter != 3:
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
    counter += 1
