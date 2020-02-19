#Find the factorial value of the given number

print("Factorial")
print("---------")

def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)          
 
number = int(input("Enter the number : "))
print(factorial(number))
