import random
ans = "Y"
while ans == "Y":
    print('choose "0" for rock,"1" for paper and "2" for scissors\n')
    a = int(input())
    b = random.randint(0, 2)

    if 0 <= a < 3:
        if a == 0:
            print("you chose rock")
            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
        elif a == 1:
            print("you chose paper")
            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)
        else:
            print("you chose scissors")
            print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)
        if b == 0:
            print("computer chose rock")
            print("""
                 _______
             ---'   ____)
                   (_____)
                   (_____)
                   (____)
             ---.__(___)
             """)
        elif b == 1:
            print("computer chose paper")
            print("""
                  _______
             ---'    ____)____
                        ______)
                       _______)
                      _______)
             ---.__________)
             """)
        else:
            print("computer chose scissors")
            print("""
                 _______
             ---'   ____)____
                       ______)
                    __________)
                   (____)
             ---.__(___)
             """)
        if (a, b) == (0, 0) or (a, b) == (1, 1) or (a, b) == (2, 2):
            print("Its a draw")
        elif (a, b) == (0, 1) or (a, b) == (1, 2) or (a, b) == (2, 0):
            print("You lose")
        else:
            print("You win")

    else:
        print(' You did not enter a valid input')
    ans = input('Do you want to play again.Enter "Y" or "N"\n')
    while ans not in ['Y', "N"]:
        print('enter a valid input')
        ans = input('Do you want to play again.Enter "Y" or "N"\n')
print("Thanks for playing.Ta Ta bye bye")

