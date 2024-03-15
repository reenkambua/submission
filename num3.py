#Write a program that takes an integer as input and returns true if the input is a power of two.

number=int (input("Enter an integer: "))
x=0
result=0

while result < number :
    result = 1 << x
    if result == number:
        print("True")
        break
    x = x +1
else:
    print("False")