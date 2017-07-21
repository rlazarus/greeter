import random

greetings = [
  "Hello",
  "hi",
  "Good morning",
  "Hey there!",
]
name = raw_input("What is your name? ")
n = random.randint(0, 3)
print greetings[n] + ", " + name + "!"
