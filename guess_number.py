from random import randint


rand_number = randint(1, 100)

while True:
    guess = int(input('Введите число: '))

    if guess == rand_number:
        print('Вы угадали!')
        break
    elif rand_number > guess:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')
