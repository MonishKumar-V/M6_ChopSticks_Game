"""
Chopsticks is a hand game for two or more players, in which players start with one finger extended in each hand and
continue playing by tabbing the opponent player's hand till one of the player has five in both hands.
The player who has five or greater in both hands lose the game and the other player wins the game

"""

# Importing random number generator
import random

# declaring the variables for the game

p_right = int(1)
p_left = int(1)
c_right = int(1)
c_left = int(1)

"""
This function is CPU function which has the gameplay instructions of the CPU.
This function covers every condition and rules of the game.
Random number generator provides the input for CPU gameplay.

"""

def computer(p_right, p_left, c_right, c_left):
    if c_left == 0 and c_right % 2 == 0 and c_right != 0:
        c_right = c_right / 2
        c_left = c_right
        print("CPU gone with splitting\n")
        print(f"Now CPU has  : right hand: {c_right} and left hand: {c_left}\n")
    elif c_right == 0 and c_left % 2 == 0 and c_left != 0:
        c_left = c_left / 2
        c_right = c_left
        print("CPU gone with splitting\n")
        print(f"Now CPU has : right hand: {c_right} and left hand: {c_left}\n")
    else:
        while 1:
            c_play = random.randint(1, 4)
            if c_play == 1 and p_right < 5 and c_right < 5:
                p_right = p_right + c_right
                print("CPU tabbed your right hand with its right hand\n")
                print(f"so now the values are right hand: {p_right} and left hand: {p_left}")
                break
            elif c_play == 2 and p_left < 5 and c_right < 5:
                p_left = p_left + c_right
                print("CPU tabbed your left hand with its right hand\n")
                print(f"so now the values are right hand: {p_right} and left hand: {p_left}")
                break
            elif c_play == 3 and p_right < 5 and c_left < 5:
                p_right = p_right + c_left
                print("CPU tabbed your right hand with its left hand\n")
                print(f"so now the values are right hand: {p_right} and left hand: {p_left}")
                break
            else:
                if p_left < 5 and c_left < 5:
                    p_left = p_left + c_left
                    print("CPU tabbed your left hand with its left hand\n")
                    print(f"so now the values are right hand: {p_right} and left hand: {p_left}")
                    break
    cpos = (p_left >= 5 and p_right >= 5) and (c_left <= 5 or c_right <= 5)
    return p_right, p_left, cpos


"""
This function is player function which has the gameplay instructions of the player.
This function covers every condition and rules of the player.
Player has to give input to play.

"""

def player(p_right, p_left, c_right, c_left):
    print("It's time for your chance\n")
    print(f"Cpu : right hand: {c_right} ,left hand :{c_left} \n")
    print(f"player: right hand : {p_right} ,left hand : {p_left} \n")

    if (p_left == 0 and p_right % 2 == 0 and p_right != 0) or (p_right == 0 and p_left % 2 == 0 and p_left != 0):
        print("you have a option to split in this situation, if you want to split enter 1 or enter 2 to tab\n")
        while 1:
            p_split = int(input("so you're choice is "))
            if p_split == 1:
                if p_right == 0:
                    p_left = p_left / 2
                    p_right = p_left
                    print(f"\nyou have split your numbers in right hand , now the values in both hands is {p_right}")
                    break
                else:
                    p_right = p_right / 2
                    p_left = p_right
                    print(f"\nyou have split your numbers in right hand , now the values in both hands is {p_right}")
                    break

            elif p_split == 2:
                if p_right == 0:
                    print("\nwhich hand of CPU you want to tab:")
                    print("\n enter 'R' for right hand 'L' for left hand \n")
                    while 1:

                        p_input = (input("which hand of CPU you want to tab :"))

                        if p_input == "R":
                            c_right = c_right + p_left
                            print(f" C_right - {c_right}")
                            break
                        elif p_input == 'L':
                            c_left = c_left + p_left
                            print(f" C_left - {c_left}\n")
                            break
                        else:
                            print("Enter valid Input:")
                    break
                else:
                    print("\nwhich hand of CPU you want to tab")
                    print("\nenter 'R' for right hand 'L' for left hand \n")
                    while 1:
                        p_input = (input("which hand of CPU you want to tab:"))

                        if p_input == "R":
                            c_right = c_right + p_right
                            print(f" C_right - {c_right}")
                            break
                        elif p_input == 'L':
                            c_left = c_left + p_right
                            print(f" C_left - {c_left}\n")
                            break
                        else:
                            print("Enter valid Input:")
                    break
            else:
                print("Enter valid input ")

    else:
        print("your turn\n")
        print("Enter 'R' for right hand 'L' for left hand\n")
        p_hand = input("your hand: ")
        c_hand = input("Cpu hand: ")
        if p_hand == 'R' and c_hand == 'R':
            c_right = c_right + p_right
            print(f"Cpu right: {c_right} ")
        elif p_hand == 'R' and c_hand == 'L':
            c_left = c_left + p_right
            print(f"Cpu left: {c_left} ")
        elif p_hand == 'L' and c_hand == 'R':
            c_right = c_right + p_left
            print(f"Cpu right: {c_right} ")
        elif p_hand == 'L' and c_hand == 'L':
            c_left = c_left + p_left
            print(f"cpu left: {c_left} ")
        else:
            print(" enter valid input\n")
    pos = (c_left >= 5 and c_right >= 5) and (p_left <= 5 or p_right <= 5)
    return c_right, c_left, pos


# This is the starting portion of the game

print("You ready to play chopsticks?\n")
print("fine,come on lets play\n")
print("call the toss either 1 or 2\n")

# Calling toss to start the game

while 1:
    toss_random = random.randint(1, 2)
    P_call = int(input("so you're calling "))
    if P_call == toss_random:
        print("it seems like you won the toss, you go first\n")
        break
    elif P_call != 1 and P_call != 2:
        print("Enter valid number to pass the toss\n")

    else:
        print("Oops, CPU won the toss so it will go first\n")
        break

# This is the condition to check if either of the players have won their game or lost

while 1:
    if P_call == toss_random:
        c_right, c_left, pos = player(p_right, p_left, c_right, c_left)
        if pos:
            print("player won")
            break
        else:
            p_right, p_left, c_pos = computer(p_right, p_left, c_right, c_left)
            if c_pos:
                print("cpu won")
                break
    else:
        p_right, p_left, c_pos = computer(p_right, p_left, c_right, c_left)
        if c_pos:
            print("cpu won")
            break
        else:
            c_right, c_left, pos = player(p_right, p_left, c_right, c_left)
            if pos:
                print("player won")
                break
