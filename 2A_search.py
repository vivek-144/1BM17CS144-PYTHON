list=[]
numbers=int(input("Enter the list length\n"))
print("Enter numbers")
for i in range(numbers):
    data=int(input())
    list.append(data)    
print(list)
search = int(input("Enter the no. to search\n"))
if search in list:
    
    print(search,"\nTrue, Element is present\n is the postion",list.index(search)+1)
else:
    print(search,"\nnot found")

