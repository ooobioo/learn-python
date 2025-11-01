# RANDOM #################################################

import random

x = random.random()

print(x)
print(10000 * x)
print(int(10000 * x))



# random.seed(2345436532)  
# seed hält die von random generierten folgen stabil - reproduziert immer die gleichen folgen

randomint = random.randint(0,10)
for i in range(1,100):
    print(random.randint(0,10), end=" ")
print()


animals = [
    "aardvark", "albatross", "alligator", "alpaca", "antelope",
    "armadillo", "baboon", "badger", "barracuda", "bat",
    "bear", "beaver", "bison", "boar", "butterfly",
    "camel", "capybara", "cassowary", "cat", "chamois",
    "cheetah", "chimpanzee", "chinchilla", "cobra", "coelacanth",
    "cougar", "cow", "coyote", "crab", "crane",
    "crocodile", "crow", "deer", "dinosaur", "dog",
    "dolphin", "donkey", "dove", "dragonfly", "duck",
    "eagle", "echidna", "eel", "elephant", "elk",
    "emu", "falcon", "ferret", "finch", "fish"
]

for i in range(1,20):
    print(random.choice(animals), end=" ")

print()
print()


for i in range(1,5):
    print(random.sample(animals, 3), end=" ")
    print()

print()

animals = [
    "aardvark", "albatross", "alligator", "alpaca"
]
for i in range(1,5):
    print(random.sample(animals, 3, counts=[3,4,1,1]), end=" ")
    print()

print()