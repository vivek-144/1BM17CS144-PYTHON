def rev1(str):
    lis1 = str.split()
    lis1.reverse()
    print(lis1)
    print(" ".join(lis1))
def rev2(str):
    lis1 = str.split()
    str2 = " "
    for i in lis1:
        str2+=i[::-1]
        str2+=" " 
    print(str2)
str = input("Enter the String \n")
rev1(str)
rev2(str)

