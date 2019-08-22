def Fibonacci(n): 
    if n<0: 
        print("wrong input") 
 
    elif n==1: 
        return 0
 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)
  

      num=int(input("enter the number : "))  

i=1
while i<num:

       print(Fibonacci(i)) 
             i=i+1
  

