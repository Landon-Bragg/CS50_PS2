Raw = input("Input: ")

print("Output:", end = '')

for letter in Raw:
    if not letter.lower() in ['a','e','i','o','u']:
        print(letter, end = "")

print()


