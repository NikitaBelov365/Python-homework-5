num = int(input('input number '))
pow = int(input('input power '))
multiplier = num

def raising(num, pow, multiplier):
    if pow == 1:
        return print(num)
    else:
        raising(num*multiplier, pow-1, multiplier)
    
raising(num, pow, multiplier)