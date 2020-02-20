#Find the sum of factorial series

print("Sum of Factorial series")
print("---------")

def sumOfSeries(num): 
    res = 0
    fact = 1
    for i in range(1, num+1): 
        fact = fact * i 
        res = res + (i/ fact) 
    return res 
  
n = int(input("Enter the number : "))
print("Sum: ", sumOfSeries(n)) 
