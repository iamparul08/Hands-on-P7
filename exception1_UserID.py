try:
    f = open('newfile1_UserID.txt', 'r')
    print(f.readlines())

except:
    print("Exception occured i.e. FileNotFoundError")

    
finally:
    print("The 'try except' is finished.")

