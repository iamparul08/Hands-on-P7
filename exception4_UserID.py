
dict3_UserID = {"k1": 10, "k2": 20, "k3": 30}
try:
    print("Resource open.")
    print(dict3_UserID["k5"])

except Exception as e:
    print(e)
    print("\nResource closed.")

finally:
    print("try catch ended.")