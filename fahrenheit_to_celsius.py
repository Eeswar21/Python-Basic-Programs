#Fahrenheit to Celsius and Celsius to Fahrenheit conversion

print("Fahrenheit to Celsius and Celsius to Fahrenheit conversion")

def celtofahr():
  '''this function is for converting temprature value from celsius to fahrenheit'''
	celsius = float(input("Enter temperature in celsius: "))
	fahrenheit = (celsius * 9/5) + 32
	print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
	
def fahrtocel():
  '''this function is for converting temprature value from celsius to fahrenheit'''
	fahrenheit = float(input("Enter temperature in fahrenheit: "))
	celsius = (fahrenheit - 32) * 5/9
	print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

while True:
  print("1.Fahrenheit to Celsius\n2.Celsius to Fahrenheit\n3.Quit\n")
  choice = int(input("Choose your option : "))
  if choice==1:
    fahrtocel()
  elif choice==2:
    celtofahr()
  else:
    break
  
print("Bye.........")
