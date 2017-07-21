import random

greetings = [
  "Hello",
  "hi",
  "Good morning",
  "Howdy",
  "Hey there!",
]
name = raw_input("What is your name? ")
n = random.randint(0, 4)
print greetings[n] + ", " + name + "!"
