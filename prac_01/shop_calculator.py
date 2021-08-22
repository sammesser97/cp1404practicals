DISCOUNT_THRESHOLD = 100

total_cost = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = int(input("Price: "))
    total_cost += price
if total_cost >= DISCOUNT_THRESHOLD:
    discount = total_cost * 0.1
    print(f"Your discount was ${discount}")
    print(f"Total price for {number} items is ${total_cost - discount}")
