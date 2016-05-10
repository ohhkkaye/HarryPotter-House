#print intro
print "Welcome to the Hogwarts!"
print "You will begin your journey by deciding your house."

#print questions
print "What is your favorite creature?"
print "Owl"
print "Mouse"
print "Snake"
print "Cat"


animal = raw_input()

if animal.lower() == "owl":
	print "Please now choose the following options:"
	print "Would you like to run to the forest or to the water?"
	
	location = raw_input()

	if location == "forest":
		print "Now you are in the forest, what do you do first? Type the number."
		print "1. Scavenge for food"
		print "2. Find tools"
		print "3. Call for help"
		print "4. Try some magic"

		task_number = raw_input()

		if task_number == "1":
			print "You in Gryffindor!"
		elif task_number == "2":
			print "You are in Ravenclaw!"
		elif task_number == "3":
			print "You are in Hufflepuff!"
		elif task_number == "4":
			print "You are in Slytherin!"
		else:
			print "You do not belong in any house!"
	
	elif location == "water":
		print "You chose water, what do you try to do? Type the number."
		print "1. Swim until you find some help."
		print "2. Use magic"
		print "3. Try to make yourself into a water creature"
		print "4. Try to make yourself fly"

		task = raw_input()

		if task == "1":
			print "You are in Hufflepuff!"
		elif task == "2":
			print "You are in Slytherin!"
		elif task == "3":
			print "You are in Gryffindor"
		elif task == "4": 
			print "You are in Ravenclaw!"
		else:
			print "You do not belong in any house!"
	else:
			print "You do not belong in any house!"

if animal.lower() == "mouse":
	print "Please choose from the following"
	print "Would you like to go into the house or into the forest?"

	location = raw_input()

	if location == "house":
		print "Now what would you try to do? Type the number."
		print "1. Scavenge for food"
		print "2. Scare the owner"
		print "3. Attract other mice"
		print "4. Go back outside"

		task = raw_input()

		if task == "1":
			print "You are in Gryffindor!"
		elif task == "2":
			print "You are in Slytherin!"
		elif task == "3": 
			print "You are in Hufflepuff!"
		elif task == "4":
			print "You are in Ravenclaw!"
		else:
			print "You do not belong in any house!"

	if location == "forest":
		print "What would you do in the forest?"
		print "1. Help other mice"
		print "2. Be smart about your decisions"
		print "3. Talk to other animals"
		print "4. Try to make a trap for food"

		task = raw_input()

		if task == "1":
			print "You are in Hufflepuff!"
		elif task == "2":
			print "You are in Ravenclaw!"
		elif task == "3":
			print "You are in Gryffindor!"
		elif task == "4":
			print "You are in Slytherin!"
		else:
			print "You do not belong in any house!"
	else:
			print "You do not belong in any house!"

if animal.lower() == "snake":
	print "You can slide into many places, where would you go?"
	print "hole or water"

	location = raw_input()

	if location == "hole":
		print "You may now use your powers, what would it be? Print number"
		print "1. escape"
		print "2. disappear into thin air"
		print "3. Snap at your enemies"
		print "4. Be a flying snake."

		powers = raw_input()

		if powers == "1":
			print "You are in Hufflepuff!"
		elif powers == "2":
			print "You are in Gryffindor!"
		elif powers == "3":
			print "You are in Slytherin!"
		elif powers == "4": 
			print "You are in Ravenclaw!"
		else:
			print "You do not belong in any house!"

	if location == "water":
		print "You chose water, what do you try to do? Type the number."
		print "1. Swim until you find some help."
		print "2. Use magic"
		print "3. Try to make yourself into a water creature"
		print "4. Try to make yourself fly"

		task = raw_input()

		if task == "1":
			print "You are in Hufflepuff!"
		elif task == "2":
			print "You are in Slytherin!"
		elif task == "3":
			print "You are in Gryffindor"
		elif task == "4": 
			print "You are in Ravenclaw!"
		else:
			print "You do not belong in any house!"
	else:
			print "You do not belong in any house!"

if animal.lower() == "cat":
	print "Where would you sleep?"
	print "couch or floor"

	location = raw_input()

	if location == "couch":
		print "Would you scratch or sleep?"

		action = raw_input ()

		if action == "scratch":
			print "You are in Slytherin!"
		elif action == "sleep":
			print "You are in Hufflepuff!"
		else:
			print "You do not belong in any house!"

	if location == "floor":
		print "Would you stretch or roll around?"

		action = raw_input()

		if action == "stretch":
			print "You are in Ravenclaw!"
		elif action == "roll around":
			print "You are in Gryffindor!"
		else:
			print "You do not belong in any house!"

	else:
		print " You do not belong to a house!"

else:
	print "You do not belong to Hogwarts"