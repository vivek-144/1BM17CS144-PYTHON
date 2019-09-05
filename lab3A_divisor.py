  
num = int(input("Enter the number : "))
i = 1
print("The divisors are : ")
while i <= num :
    if num%i == 0 :
        print(i)
    i = i+1
