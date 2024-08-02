def fibonacci_generator(number):
    num1 = 0
    num2 = 1
    while num1 + num2 <= number:
        yield num1
        yield num2
        yield num1 + num2

for i in fibonacci_generator(21):
    print(i)