
num1_UserID = int(input("Enter 100 "))

try:
    print("Resource open.")
    sum1_UserID = num1_UserID + num2_UserID
    print(sum1_UserID)

except Exception as e:
    print(e)
    print("\n Resource closed.")

finally:
    print("Try catch ended.")