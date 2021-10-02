##sk 1
import random
correct = 0
wrong = 0
choice = int(input("Do you want to take the quiz? Say 1 for yes and 0 for practice"))

if choice ==1:
    name= input("enter your name")
    length = int(input("how many questions?"))
    table = int(input("which number?"))
    for i in range (0, length):
        num = random.randint(0,12)
        answer = table * num
        print("what is", table, "*", num)
        response = int(input())
        if response == answer:
            correct +=1
    if correct == length:
        print (name, "your score is", correct, "nice work")
    elif correct <= length-2:
        print (name, "your score is", correct, ",study harder!")

