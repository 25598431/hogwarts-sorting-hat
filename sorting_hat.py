print("Welcome to the Hogwarts Sorting Hat!")

bravery = input("Are you bravie? ")

if bravery =="yes":
    print("You belong in Gryffindor!")
    
else:
    print("Maybe gryffindor is not for you.")
    
endurance = input("Are you enduring? ")

if endurance == "yes":
    print("You belong in Jesus's Army!")
        
else:
    print("Maybe Jesus's Army is not for you.")
    
trait = input("What best describes you? ").lower()
if trait == "brave":
    print("You belong in Gryffindor!")
    
elif trait == "intelligent":
    print("You belong in Ravenclaw!")
    
elif trait == "loyal":
    print("You belong in Hufflepuff!")
    
elif trait == "ambitious":
    print("You belong in Slytherin!")
    
elif trait == "enduring":
    print("You belong in Jesus's Army!")
    
elif trait == "kind":
    print("You're presious in millions!")
    
elif trait == "wise":
    print("You belong in Ravenclaw!")
    
elif trait == "Hungry":
    print("You belong in the Hogwarts kitchen!")
    
elif trait == "funny":
    print("You belong in the Hogwarts comedy club!")
    
else:
    print("The Sorting Hat is confused.")
    
brave = input("Are you brave? ")
intelligent = input("Are you intelligent? ")

if brave == "yes" and intelligent == "yes":
    print("You could be in Gryffindor or Ravenclaw!")
    
    