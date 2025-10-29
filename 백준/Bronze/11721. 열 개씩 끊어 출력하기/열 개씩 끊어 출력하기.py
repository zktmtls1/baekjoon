import sys

text = input()

for i in range (1+len(text)//10):
    print(text[i*10:i*10+10])