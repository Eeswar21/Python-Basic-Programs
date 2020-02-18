#Display the first n terms of Fibonacci series

print("Fibonacci series")

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
 
number = int(input("Enter the number : "))
 
for count in range(number):
    print(fibonacci(count), end=",")
