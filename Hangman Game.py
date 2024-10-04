import random
answer = "yes"
while answer == "yes":
    print("Welcome to the hangman game.You have only 6 tries. ")
    list = ["apple", "dictionary", "triangle", "bharat", "mango", "america", "police", "brother","fire", "organic","ghost"]
    a = random.choice(list)
    l = []
    new_list =['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    max = 0
    for i in range(0,len(list)):
        if len(list[i]) > max:
            max = len(list[i])
    for i in range(0,max):
        l.append(" ")
    wrong_moves = 0
    while wrong_moves <= 5:
        b = input("\nenter a letter \n")
        if b not in a:
            wrong_moves += 1
            print(f"The number of wrong moves = {wrong_moves}")
            print(new_list[wrong_moves])
        for i in range(0, len(a)):
            if b == a[i]:
                l[i] = a[i]
            else:
                l[i] = "_"
        for i in l:
            print(i, end='')
        while wrong_moves <= 5:
            b = input("\nenter a letter \n")
            if b not in a:
                wrong_moves += 1
                print(f"The number of wrong moves = {wrong_moves}")
                print(new_list[wrong_moves])
            for i in range(0, len(a)):
                if b == a[i]:
                    l[i] = a[i]
            for i in l:
                print(i, end='')
        print("\nGame over")
        break
    answer = input('Do you want to play the game again? Enter "yes" or "no".')