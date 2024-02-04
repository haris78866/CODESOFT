import math

print('Simple calculator')
print('1) Addition')
print('2) Subtraction')
print('3) Multiplication')
print('4) Division')
print('5) Modulus')
print('6) Exit')

choice = int(input('Enter your choice: '))

if choice in [1, 2, 3, 4, 5]:
    x = float(input('Enter the value of variable(x): '))
    y = float(input('Enter the value of variable(y): '))

    def calculation(x, y, choice):
        if choice == 1:
            print('Addition x:', x, '& y:', y)
            return x + y
        elif choice == 2:
            print('Subtraction x:', x, '& y:', y)
            return x - y
        elif choice == 3:
            print('Multiplication x:', x, '& y:', y)
            return x * y
        elif choice == 4:
            print('Division x:', x, '& y:', y)
            return x / y
        elif choice == 5:
            print('Modulus x:', x, '& y:', y)
            return x % y

    output = calculation(x, y, choice)
    print('Result:', output)

elif choice == 6:
    print('Exiting the calculator.')

else:
    print('Invalid choice. Please enter a number between 1 and 6.')
