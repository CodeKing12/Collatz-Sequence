#This code uses the collatz sequence which can turn any integer into 1 by repetitively performing one of two operations on the number

def collatz(number):
    if number % 2 == 0:
        operated_number = number // 2
    else:
        operated_number = 3 * number + 1
    return operated_number

print("What number would you like to collatz?")
try:
    inputted_number = int(input())
except ValueError: #Checks if input is a number and not a string
    print("Your input must be an integer")

collatz_seq = collatz(inputted_number)
print(collatz_seq)

#Recalls function till the return value is 1
while collatz_seq != 1:
    previous = collatz_seq
    collatz_seq = collatz(previous)
    print(collatz_seq)