
num1_UserID = int(input("Enter 100"))
num2_UserID = int(input("Enter 0"))
try:
    print("\nResource open")
    div1_UserID = num1_UserID / num2_UserID

except Exception as e:
    print("Hey, you can not divide by zero", e)
    print("\nResource closed.")

finally:
    print("try catch ended.")