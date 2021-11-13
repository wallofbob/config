#THE CONDITION IN PYTHON IS EXCLUSIVE
#Task 1
playerno = int(input("enter the number of players"))
while playerno <2 or playerno> 5:
    playerno = int(input("enter the number of players, it should be between 2 and 5"))

playernames = []
for i in range (playerno):
    name = input("Enter the name of the player")
    playernames.append(name)


holeno = int(input("enter the number of holes, 9 or 18 "))
while holeno != 18 or holeno !=9: 
    holeno = int(input("enter the number of holes, it should be 9 or 18" ))

par = int(input("enter the par"))

#printing output
print (f'the number of players is {playerno} \n the names of the players are {playernames} \n the par is {par} \n the number of holes is {holeno}')

print (f'the par is {par}')

check = input("is all the info right? enter y or n")
if correct.lower() = n:
    fix = int(input("enter 1 for number of players, 2 for names of players, 3 for number of holes, or 4 for the par"))
    if fix ==1:
        playerno=int(input("enter the number of players"))
    elif fix ==2:
        playernames.clear()
        for i in range (playerno):
            name = input("enter the name")
            playernames.append(name)
    elif fix ==3:
        holeno=int(input("enter the number of holes"))
    elif fix ==4:
        par = int("enter the par")


