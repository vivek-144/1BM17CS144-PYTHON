a=int(input("ENter the number of array elements"))
arr=[]
even=[]

for x in range(a):
    arr.append(int(input("Enter number\n")))
for x in arr:
    if (x%2==0):
        even.append(x)

print(arr)
print(even)
