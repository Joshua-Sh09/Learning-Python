print('Calculator')
print('Pick A Number: ')
num1 = int(input())
print('Pick Another Number:')
num2 = int(input())
print('Please Choose A Option:','(add, subtract, multiply, divide)')
option = input().strip().lower()
if option in ['+', 'add', 'sum', 'addition']:
    print("your answer is:", num1 + num2)
elif option in['-', 'subtracts', 'minus', 'decrese', 'reduced']:
    print("your answer is", num1 - num2)
elif option in ['x', 'multiply', 'times','*']:
    print("your answer is", num1 * num2)
elif option in [ '/', 'by', 'divide']:
    if num2 != 0:
     print("your answer is", num1 / num2 )
    else:
          print("error divition with zero is not allowed")
else:
    print('invalid option please try again')

