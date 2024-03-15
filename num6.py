#Write a program that counts the number of vowels in a sentence.

sentence=(input("write a sentence:"))
vowels=("a","e","i","o","u","A","E","I","O","U")
count=0
for char in sentence:
    if(char in vowels):
        count=count+1
    
print(count)
