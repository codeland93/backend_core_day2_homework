attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

vegetarian = input("Do you want vegetarian food? (yes/no): ").strip().lower()
caterer = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"
print(caterer)

