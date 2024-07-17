place = input("Choose a place: forest or cave? ")

if place == 'forest':
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        pass
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == 'cave':
    action = input("Do you want to light a torch or proceed in the dark")
    if action == "light a torch":
        print("You found a chest!")
    elif action == "proceed in the dark":
        pass
        print("Opps you met a monster!") 
