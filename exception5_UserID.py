list3_ADID = [10, 20, 30, 40, 50]
try:
    print("Resource open.")
    print(list3_ADID[7])

except Exception as e:
    print(e)

finally:
    print("Resource closed.")

