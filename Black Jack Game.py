import os
import random
print("Welcome to the Black Jack game ")


all_cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
# List of all the cards in the game


your_cards = random.sample(all_cards, 2)    # This is a list of the player's cards.
print(f'Your cards are {your_cards}')


def you_total(your_cards):   # This gives the sum of all cards of the player.
    your_total = sum(your_cards)
    return your_total


print(f'Your total is {you_total(your_cards)}')


computer_cards = random.sample(all_cards,1)   # This is a list of computer's cards.
print(f'Computer\'s cards are {computer_cards}')


def comp_total(computer_cards):   # This gives the sum of all the cards of the computer.
    computer_total = sum(computer_cards)
    return computer_total
print(f'Computer\'s total is {comp_total(computer_cards)}')




def play(your_cards,computer_cards):
    a = input("do yu want to draw card 'yes' or 'no'? ")
    if a == "no":
        while comp_total(computer_cards) < 16:
            computer_cards.append(random.choice(all_cards))
        print(f'Computer\'s cards are {computer_cards}')
        system_total = comp_total(computer_cards)
        player_total = you_total(your_cards)
        print(f'computer\'s total is {system_total}')
        if system_total > 21:
            print("You win")
            return None
        else:
            if system_total > player_total:
                print("You lose")
                return None
            elif system_total == player_total:
                print("Its a draw. ")
                return None
            else:
                print("You win")
                return None
    elif a == "yes":
        player_total = you_total(your_cards)
        your_cards.append(random.choice(all_cards))
        player_total = you_total(your_cards)
        print(f'Your cards are {your_cards}')
        print(f'your total is {player_total}')

        while player_total < 16:
            print("As your cards sum was < 16, we addded more cards.")
            your_cards.append(random.choice(all_cards))
            player_total = you_total(your_cards)
            print(f'Your cards are {your_cards}')
            print(f'your total is {player_total}')
        
        
        if player_total > 21:
                print("you lose")
                return None
        else:
            reply = input("Do you want to draw another card? \n")
            if reply == "no":
                system_total = comp_total(computer_cards)
                player_total = you_total(your_cards)
                while system_total < 16:
                    print("As the sum of computer\'s cards < 16, we added more cards. ")
                    computer_cards.append(random.choice(all_cards))
                    system_total = comp_total(computer_cards)
                print(f'Computer\'s cards are {computer_cards}')
                print(system_total)
                system_total = comp_total(computer_cards)
                if system_total > 21:
                    print("You win")
                    return None
                else:
                    if system_total > player_total:
                        print("You lose")
                        return None
                    elif system_total == player_total:
                        print("Its a draw. ")
                        return None
                    else:
                        print("You win")
                        return None
            elif reply == "yes":
                your_cards.append(random.choice(all_cards))
                print(f'Your cards are {your_cards}')
                player_total = you_total(your_cards)
                print(player_total)
                play(your_cards,computer_cards)
    else:
        print("You entered a wrong input")
        return None
    

ans = "yes"
while ans == "yes":
    play(your_cards,computer_cards)
    ans = input("Do you want to play again? ")
    if ans == "yes":
        os.system('cls' if os.name == 'nt'else'clear')