#Grade Calcution - total subjects are 3

print("Grade Calculation")

def total():
  '''this function is for total marks obtained by students'''
  global total_mark
  total_mark = subject1 + subject2 + subject3
  print('Total Mark: %0.2f' %(total_mark))
	
def percentage():
  '''this function is for finding percentage  marks obtained by students'''
  global percentage_mark
  percentage_mark = total_mark/3
  print('Average Mark: %0.2f' %(percentage_mark))

def grade():
  '''this function is for finding grade based on the average marks'''
  if percentage_mark>=80:
    print("Grade : A")
  elif percentage_mark>=70 and percentage_mark<80:
    print("Grade : B")
  elif percentage_mark>=60 and percentage_mark<70:
    print("Grade : C")
  elif percentage_mark>=50 and percentage_mark<60:
    print("Grade : D")
  else:
    print("Grade : E")

while True:
  subject1=int(input("Enter the subject1 mark : "))
  subject2=int(input("Enter the subject2 mark : "))
  subject3=int(input("Enter the subject3 mark : "))
  if subject1>100 or subject2>100 or subject3>100:
    print("Mark should not exceeds the value of 100")
  else:
    total()
    percentage()
    grade()
  action=input("Press C for continue or Press Q for quit(C/Q) : ")
  if action=='Q' or action=='q':
    break
