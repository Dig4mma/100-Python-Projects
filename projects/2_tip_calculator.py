# Welcome to Tip Calculator

print("Welcome to the tip calculator!")
bills = round(float(input("What was the total bill? ")), 2)
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

totalShare = bills / people
tipShare = totalShare * tip / 100
share = round(totalShare + tipShare, 2)
print(f"Each person should pay: ${share}")
