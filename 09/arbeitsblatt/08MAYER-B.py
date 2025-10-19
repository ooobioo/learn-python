# 1 #############################################
print("# 1 #################")
import random

def random_int():
    return random.random()

for i in range(1,10):
    print("Random number:", int(1000*random_int()), end=" ")
print()

for i in range(1,10):
    print("Random number:", random.randint(1,1000), end=" ")
print()


# 2 #############################################
print("# 2 #################")

def random_int5():
    rand = 1
    while rand%5 != 0:
        rand = random.randint(1,1000)
    
    return rand

print("Random number divisible by 5: ", random_int5())


# 3 #############################################
print("# 3 #################")

import time
import threading

def wuerfelfolge(k=2):

    def spinner():
        symbols = ['|', '/', '-', '\\']
        idx = 0
        while not done:
            print(f'\r{symbols[idx % len(symbols)]} I\'m rolling the dice...', end='')
            idx += 1
            time.sleep(0.1)
        print(end="\r")
    
    done = False
    spinner_thread = threading.Thread(target=spinner)
    spinner_thread.start()

    counter = 0
    last_equal_series = []

    while len(last_equal_series) < k:
        round = random.randint(1,6)
        if round not in last_equal_series:
            last_equal_series.clear()
        last_equal_series.append(round)
        counter += 1

    done = True
    spinner_thread.join()

    print("Series: ",last_equal_series)
    return f"{counter:,}".replace(',', '.')

print("Dice rolls:", wuerfelfolge(10))


# 4 #############################################
print("# 4 #################")

def wuerfelfolge2(k=2):
    wuerfe_pro_zahl = [0,0,0,0,0,0]
    while max(wuerfe_pro_zahl) < k:
        round = random.randint(1,6)
        wuerfe_pro_zahl[round-1] += 1
    print("Scoreboard: ",wuerfe_pro_zahl)
    return sum(wuerfe_pro_zahl)

print("Dice rolls:", wuerfelfolge2(100))


# 5 #############################################
print("# 5 #################")

def wurfelspiel():

    def eingabe():
        liste = []
        user_input = ""
        while True:
            user_input = input("Enter a number between 1 and 99 (or type \"End\" to finish): ")
            if user_input.lower() == "end":
                break
            try:
                if int(user_input) not in range(0,100):
                    print("Invalid input – the value must be between 0 and 99.")
                    continue
                liste.append(user_input)
            except Exception as e:
                print(f"Something's wrong with your input: {user_input} - {e} ")
        
        return liste


    def initialisieren():
        liste = []
        while len(liste) < 5:
            liste.append(random.randint(1,99))
        print(liste)

        return liste

    def spielen(liste: list):
        punkte = [0,0]

        user_selection = input(f"Please select a number from 1 to {len(liste)}: ")
        user_selection = int(user_selection)
        print("You selected ", liste[user_selection-1])

        while max(punkte) < 5:
            computer1 = random.randint(0,len(liste))
            computer2 = random.randint(0,len(liste))
            if(computer1 == computer2):
                punkte[1] += 1
            if user_selection == computer1:
                punkte[0] += 1

        if punkte[0] > punkte[1]:
            print(f"You won {punkte[0]}:{punkte[1]}")
        else:
            print(f"Computer won {punkte[1]}:{punkte[0]}")

        return
    

    users_list = eingabe()
    if len(users_list) < 2:
        users_list = initialisieren()
    spielen(users_list)


wurfelspiel()