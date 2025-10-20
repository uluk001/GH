name = input("Guest name: ")
people = int(input("People in group: "))
money = float(input("Amount to pay: "))
tip = float(input("Tip % (20, 22, 25): "))

total = money + money * tip / 100
print(f"\n{name}, total amount: ${total:.2f}")

pay = total / people
print(f"Each person pays: ${pay:.2f}")

if tip > 20:
    print("Thank you for your generosity!")
