num = 29  
primo = True
divisor = 2

if num < 2:
    primo = False

while divisor * divisor <= num:
    if num % divisor == 0:
        primo = False
        break
    divisor += 1

print(primo)