num1 = int(input('input number '))
num2 = int(input('input number '))

def summ(num1, num2):
    if num2 == 0:
        return print(num1)
    else:
        summ(num1+1, num2-1)
        
summ(num1, num2)
