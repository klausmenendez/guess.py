# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print("Enter the integer for the player to guess")
num=int(input())
print("Enter your guess")
guess=int(input())
counter=0
while guess!=num:
 if num<guess:
    print("Too high-Try Again")
    counter+=1
    guess=int(input())
 elif num>guess:
    print("Too low-Try Again")
    guess=int(input())
    counter+=1
if num==guess:
   print("You guessed it in", counter, "tries")
