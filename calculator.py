#pyhton Calculator
operator=input("Select your sign between them(+,-,*,/): ")
num1= float(input("Enter Your first number : "))
num2= float(input("Enter Your second number : "))
if operator == "+":
  result= num1 + num2
  print( round(result,2))
elif operator== "-":
      result= num1 - num2
      print( round(result,2))
elif operator== "*":
       result= num1 * num2
       print( round(result,2))
elif operator== "/":
        result= num1 / num2
        print( round(result,2))
else:
      print(f"Your (operator) is NOT Valid!")