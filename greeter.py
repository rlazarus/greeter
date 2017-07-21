import random

greetings = [
  "Hello",
  "hi",
  "Good morning",
]
name = raw_input("What is your name? ")
n = random.randint(0, 2)
print greetings[n] + ", " + name + "!"
