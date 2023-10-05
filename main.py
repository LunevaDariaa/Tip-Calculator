bill = float(input("Welcome to the tip calculator\nWhat was the total bill?  $"))
tip = int(input("What percentage tip would you like to give? 10, 15 or other?  "))
percentage = (tip / 100) + 1
split_by = int(input("How many people to split the bill?  "))
bill_plus_tip = (bill * percentage)
pay = round(bill_plus_tip / split_by, 2)
print(f"Each person should pay:  ${pay}")