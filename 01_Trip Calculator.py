#단축키변경

print("Welcome to the trip calculator!")
100
#Ask for inputs
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#Calculate the total bill including tip
total_tip = (bill * (tip / 100))
total_bill_person = (bill + total_tip) / people
total_bill = round(total_bill_person, 2)

print(f"Each person should pay: ${total_bill}")