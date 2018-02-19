first_value= input('Enter first operand: ')

second_value= input('Enter second operand: ')

operator= input('Enter operator: +, -, *, /\n')

if operator in ('+', '-', '*', '/'):

   if operator=='+':
    result= int(first_value)+ int(second_value)

   elif operator=='-':
    result= int(first_value)- int(second_value)

   elif operator=='*':
    result= int(first_value)* int(second_value)

   elif operator=='/':
    result= int(first_value)/ int(second_value)

   print('Result:', result)

else:
    print('Result: NaN')
