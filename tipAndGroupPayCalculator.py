
print("Welcome to the tip calculator")

total=float(input("What was the total bill? "))
groupCount=int(input("How many people are in your group? "))
tipAmount=float(input("What percentage would you like to tip?"))

final=(total+(total*(tipAmount*0.01)))/groupCount

print(f"Each person should pay {final}")
