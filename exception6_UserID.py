num1_ADID = int(input("Enter 100"))
num2_ADID = int(input("Enter 85"))

try:
    print("Resoure open.")
    sub1_ADID = num2_ADID - num1_ADID
    print("Substract first from second: ", sub1_ADID)

except Exception as e:
    print(e)

finally:
    print("Resource closed.")