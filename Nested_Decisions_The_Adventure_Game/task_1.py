place = input("Choose a place: forest or cave? ")

if place == 'forest':
    print("You are in a forest.")
    action = input("Do you want to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  
elif place == 'cave':
    print("You are in a cave.")
    action = input("Do you want to light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You found a chest!")
    elif action == "proceed in the dark":
        print("Oops, you met a monster!")
    else:
        pass  
else:
    print("Invalid option. Please choose either 'forest' or 'cave'.")
    action = input("Do you want to light a torch or proceed in the dark? ")
    pass 