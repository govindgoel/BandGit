import string

a=list("")
alpha = str("abcdefghijklmnopqrstuvwxyz")
message=input("Enter Key?")
x=len(message)
y=0
z=0
for counter in range(x):
    y=y+1
    letter = alpha.find(message[z:y])
    z=z+1
    letter=letter-13
    if letter < 0:
        letter=24+letter
    letter=alpha[letter:letter+1]
    if counter != x-1:
        print(letter,end="")
    else:
        print(letter)
