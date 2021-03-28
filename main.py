a = int(input())
b = int(input())
operator = input()
if operator == '-':
    print(a - b)
elif operator == '+':
    print(a + b)
elif operator == '*':
    print(a * b)
elif operator != '-' and operator != '+' and operator != '*' and operator != '/':
     print('Операция невозможна')
if operator == '/':
   if b > 0:
    print(a / b)
   else:
        print('На ноль делить нельзя')
