def primeNum():
    start =int(input("enter the start : "))
    end =int(input("enter the end : "))
    for n in range(start ,end + 1):
       if n > 1:
           for i in range(2,n):
               if (n%i) == 0:
                   break
           else:
               print(n)
print(primeNum())
