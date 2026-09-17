p = float(input("Enter principal: "))
r = float(input("Enter annual interest rate (%): "))
t = float(input("Enter time (years): "))

amount = p * (1 + r / 100) ** t
compound_interest = amount - p

print("Compound Interest:", compound_interest)
print("Total Amount:", amount)

