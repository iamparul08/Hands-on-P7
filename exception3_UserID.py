
try:
    num1_UserID = int(input("Enter 100 "))
    sum1_UserID = num1_UserID + num2_UserID
    print(sum1_UserID)

except:
    print("NameError exception generated.")

finally:
    print("try catch ended.")