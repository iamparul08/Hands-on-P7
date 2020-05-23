
try:
    num1_UserID = int(input("Enter 100"))
    num2_UserID = int(input("Enter 0"))
    print("\nResource open")
    div1_UserID = num1_UserID / num2_UserID

except ZeroDivisionError as e:
    print("Hey, you can not divide by zero", e)

except ValueError as e:
    print("Invalid input", e)

finally:
    print("\nResource closed.")