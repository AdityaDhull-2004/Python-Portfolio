import os
import random
logo = """
  _    _ _       _                 _                            
 | |  | (_)     | |               | |                           
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|   
            __/ |                                               
           |___/                                                
"""
 
 
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print(logo)
print("Welcome to the higher lower game.")



list_new = {"Justin bieber" : 111.6
,"Cristiano Ronaldo" : 110
,"Narendra Modi" : 92.7
,"YouTube" : 79.4
,"Nasa" : 77.7
,"Twitter" : 67
,"Bill Gates" : 64.1
,"Neymar" : 63
,"Virat Kohli" : 58.6
,"BarackObama" : 132
,"taylorswift" : 94.6
,"DonaldTrump" : 87.4
,"BTS" : 48.5
,"LeBron James" : 52.7
,"Amitabh Bachchan" : 48.6
,"Akshay Kumar" : 46.2
,"Salman Khan" : 45.4
,}


list_2 = []

for i in list_new :
    list_2.append(i)


def play():
    your_score = 0
    ans = "yes"
    while ans == "yes":
        a = random.choice(list_2)
        b = random.choice(list_2)
        if list_new[a] > list_new[b]:
            max_person = a
        else:
            max_person = b

        print(a)

        print(vs)

        print(b)

        print("Who do you think has more followers on twitter? ")

        guess = input("just enter the name.\n")
        
        if guess == max_person:
            
            print("You guessed it right ")
            os.system('cls' if os.name == 'nt'else'clear')
            your_score += 1
            print(logo)
            print(f'Your score is {your_score}')
            ans = "yes"
        else:
            print(f'Your score is {your_score}')
            print("You guessed it wrong")
            reply = input("Do you want to play the game again?\n")
            if reply == "yes":
                os.system('cls' if os.name == 'nt'else'clear')
                play()
            else:
                return None

play()
os.system('cls' if os.name == 'nt'else'clear')