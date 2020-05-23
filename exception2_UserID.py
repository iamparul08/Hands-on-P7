try:
    num1_UserID = int(input("Enter 100"))
    num2_UserID = int(input("Enter 0"))

    div1_UserID = num1_UserID / num2_UserID

except:
    print("ZeroDivisionError is raised")

finally:
    print("try catch ended.")