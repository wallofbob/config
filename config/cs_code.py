#THE CONDITION IN PYTHON IS EXCLUSIVE
#Task 1
playerno = int(input("enter the number of players"))
while playerno <2 or playerno> 5:
    playerno = int(input("enter the number of players, it should be between 2 and 5"))

playernames = []
for i in range (playerno):
    name = input("Enter the name of the player ")
    playernames.append(name)


holeno = int(input("enter the number of holes, 9 or 18 "))
while holeno != 18 or holeno !=9: 
    holeno = int(input("enter the number of holes, it should be 9 or 18" ))

par = int(input("enter the par"))

#printing output
print (f'the number of players is {playerno} \n the names of the players are {playernames} \n the par is {par} \n the number of holes is {holeno}')

print (f'the par is {par}')

check = input("is all the info right? enter y or n")
if check.lower() == 'n':
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

print('fyi')
for i in range(playerno):
    print(f'player {i} is {playernames[i]}')

# task 2
scores = []
for i in range (holeno):
    print (f'hole {i}')
    for i in range(playerno):
        tempscore=int(input(f'{playernames[i]} input your stroke no.'))
        tempscore2=int(input(f'do it again to confirm'))
        while tempscore2 != tempscore or tempscore != tempscore2:
            tempscore2=int(input(f'{playernames[i]} input your stroke no.'))
        scores.append(tempscore2)
        choice=input("do you want to see your scores? 'yes', 'no' or 'all' for all")
        if choice == 'all':
            print (scores)
        elif choice =='yes':
            numchoice=int(input("which playerno?"))
            print (scores[numchoice])

#task 3
for i in range (playerno):
    print (playernames[i])
    if scores[i]-par <0:
        print(f"the score is{abs(scores[i]-par)} below par")
    elif scores[i]-par>0:
        print(f"the score is{scores[i]-par} above par")
    else:
        print(f"the score is on par")

winner = min(scores)
print(f'the winner is {playernames[winner]}, and their score is {scores[winner]}')
print(f'the average is {sum(scores)/len(scores)}')


