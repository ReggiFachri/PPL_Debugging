print("===DASPRO LOGIN===\n")
try:
    i = 0
    while i < 3:
        username = input("Username : ")
        password = input("Password : ")
        
        if username == "1202228407" and password == "PPLIsFun2022":
            print("\nSuccessfully logged in!\n")
            break
        elif len(password) < 8:
            raise NameError()
        elif username != "1202228407" and password != "PPLIsFun2022":
            print("\nWrong username and password!\n")
        elif username != "1202228407":
            print("\nWrong username!\n")
        elif password != "PPLIsFun2022":
            print("\nWrong password!\n")
        i+=1
    
except NameError:
    print("\nPassword length should be more than 8 letter!\n")