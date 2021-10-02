physics = 0
chemistry = 0
history = 0
geography = 0
cs = 0
names = []
for i in range (3):
	name_inp = input("enter the name of the student")
	names.append(name_inp)
	choice = input("enter 1 for physics, 2 for chemistry, 3 for history, 4 for geography, and 5 for cs")
	if choice ==1:
		physics = physics + 1
	if choice ==2:
		chemistry = chemistry + 1

print (physics)

