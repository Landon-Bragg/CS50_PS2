grocery = {}

while True:
    try:
        #get user input
        item = input().lower()
        #check if item is in the dictionare
        if item in grocery:
            # If it is, add 1 to the count of items
            grocery[item] += 1
            # Or else add the item for the first time
        else:
            grocery[item] = 1
    except EOFError:
        # Print all the items in alpha order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
            #Stop the while loop
        break

