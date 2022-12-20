print("===DIVIDING CALCULATOR===\n")
try:
    num1 = int(input("Insert the number : "))
    num2 = int(input("Insert the dividers : "))

    if num2 == 0:
        hasil = "Can't divide a number by 0!"
    else:
        hasil = int(num1/num2)
        hasil = "The result is "+str(hasil)
        
    print(hasil)

except ValueError:
    print("Inputted data should be in integer")