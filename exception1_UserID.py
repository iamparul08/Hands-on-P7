try:
    print("resource open")
    f = open('newfile1_UserID.txt', 'r')
    print(f.readlines())
    f.close()

except Exception as e:
    print("Hi,file is unavailable.", e)
    print("resource closed")

finally:
    print("The 'try except' is finished.")

