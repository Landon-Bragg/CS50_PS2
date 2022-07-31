## Make a dictionary for all 12 months of the year (assign to numbers?)
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    ## Ask the user for the date in middle endian order 
    date = input("Date: ")
    try:
        #Change middle endian order to anno domini
        ## Split the string into (yyyy-mm-dd)
        month, day, year = date.split("/")
        if (int(month) >= 1 and int(month) <=12) and (int(day) <= 31):
            break
    except:
        try:
            #Split the date by space
            old_month, old_day, year = date.split(" ")
            #find the number that correlates to each month
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
            #remove comma from day variable
            day = old_day.replace(",","")
            #check if month is between 1 and 12 and day is between 1 and 31
            if (int(month) >= 1 and int(month) <=12) and (int(day) <= 31):
                break
        except:
            #go to the next line
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")



