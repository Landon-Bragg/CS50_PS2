while True:

    fuel = input("Fraction: ")
    try:
        numerator, denominator = fuel.split("/")

        new_numerator = int(numerator)
        new_denominator = int(denominator)

        fraction = new_numerator/new_denominator

        if fraction <= 1:
            break

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except zsh:
        pass

percent = int(fraction * 100 )

if percent <= 1:
    print("E")
if percent >= 99:
    print("F")
else:
    print(f"{percent}%")
