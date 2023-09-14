                     #1
print ("hello world")

             #2
import random

word = "key"
result = ''.join([letter * random.randint(1, 2) for letter in word])
print(result)

               #3
word = "машина"
reversed_word = word[::-1]
print(reversed_word)

                                   #4
input_string = "202, 404, 303, 707"

numbers = input_string.split(", ")

numbers = [int(number) for number in numbers]

sorted_numbers = sorted(numbers)

sorted_string = ", ".join(map(str, sorted_numbers))

print(sorted_string)
           #5
while True:
    оператор = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ")

    if оператор == 'q':
        break

    if оператор not in ('+', '-', '*', '/'):
        print("Неправильна операція. Спробуйте ще раз.")
        continue

    try:
        число1 = float(input("Введіть перше число: "))
        число2 = float(input("Введіть друге число: "))

        if оператор == '+':
            результат = число1 + число2
        elif оператор == '-':
            результат = число1 - число2
        elif оператор == '*':
            результат = число1 * число2
        elif оператор == '/':
            if число2 == 0:
                raise ZeroDivisionError("На нуль ділити не можна")
            результат = число1 / число2

        print(f"Результат: {число1} {оператор} {число2} = {результат}")
    except ValueError:
        print("Неправильний формат чисел. Спробуйте ще раз.")
    except ZeroDivisionError as e:
        print(e)


