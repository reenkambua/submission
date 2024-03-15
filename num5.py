#Write a program that takes an integer as input and returns an integer with reversed digit ordering.


number=int(input("Enter an integer number: "))
reverse_number=0
isNegative=False
if number<0:
    isNegative=True
    number=-number
    
while number !=0:
    rem=number % 10
    reverse_number=reverse_number * 10 + rem
    number=number//10
    
if isNegative:
    reverse_number=-reverse_number
print(reverse_number)

    
