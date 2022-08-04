import inflect

p = inflect.engine()
#create a list to keep a track of names
names = []

while True:
    #Get user input
    try:
        name = input("Name: ")
        names.append(name)


    except EOFError:
        print()
        break

#print the inflect module
output = p.join(names)
print("Adieu, adieu, to " + output)
