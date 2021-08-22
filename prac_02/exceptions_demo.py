"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When you enter an invalid integer, such as the letter "a"
2. When will a ZeroDivisionError occur?
    When you try to divide an integer by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")