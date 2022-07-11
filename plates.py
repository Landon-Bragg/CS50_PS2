def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #vanity plates must contain between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False
    #All vanity plates must begin with 2 letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    #First number cannot be 0
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
    #Numbers cannot be in middle of plate
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    # No periods, spaces, or punctuation allowed
    if s.isalnum():
        return True
    else:
        return False

main()