def say_about():
    print('Привет, я Томирис!')
    print('Я персональный помощник.')
    print('Я ещё маленькая,')
    print('но постоянно расту и умнею:')
    print('ведь мой код каждый день дописывают!')


say_about()


def print_friends_count(friends_count):
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)


def lets_go(name='Айбек', target='учить Python'):
    print(name + ', пойдем ' + target)


lets_go()


def lets_go(name='Друг', target='Учить Python'):
    print(name + ', пойдём ' + target)


lets_go(target='читать следующий урок!')


def multiply(a, b):
    print(a * b)


multiply(2, 3)


def print_multyply_table(a):
    for i in range(1, 11):
        print(a, '*', i, '=', a * i)


print_multyply_table(333)


def number_of_occurences(word, letter):
    result = 0
    for i in word:
        if i == letter:
            result = result + 1
    print(result)


number_of_occurences('Hello World', 'p')


def lets_go(name='Друг', target='Учить Python'):
    print(name + ', пойдём ' + target)


lets_go(target='читать следующий урок!')
lets_go(target='питон')


def multiply_sum(numbers):
    result = 1
    for i in numbers:
        result = result * i
    print(result)


def snow_date(date, month, year):
    print('Дата:', str(date) + '.' + str(month) + '.' + str(year))


snow_date(6, 7, 2023)


def rooms_equal(room_size, room_list):
    count = 0
    for room in room_list:
        if room == room_size:
            count = count + 1
    print('Комнат площадью', room_size, 'кв.м:', count)


flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]
hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]
rooms_equal(9.2, hut)
rooms_equal(5.55, flat)


def number_of_occurrences(char, string):
    count = 0
    for letter in string:
        if letter == char:
            count = count + 1
    print('Исходная строка:', string)
    print('Количество вхождений символа', char, 'составляет:', count)


phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'
number_of_occurrences('е', phrase)


def count_vowels(string):
    letters = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for letter in string:
        if letter in letters:
            count = count + 1
    print(count)


text = input('Текст: ')
count_vowels(text)


def comfort_count(target, temperatures):
    count = 0
    for comfort in temperatures:
        if comfort == target:
            count = count + 1
    print(count)


may_2022 = [26, 19, 13, 17, 20, 24, 12, 17, 21, 19, 20, 23, 26, 25, 24,
            27, 26, 18, 20, 25, 31, 20, 22, 28, 30, 34, 31, 16, 27, 30, 24]
may_2023 = [12, 12, 15, 17, 22, 25, 27, 29, 21, 24, 27, 21, 25, 13, 20,
            23, 24, 12, 19, 23, 24, 26, 24, 25, 27, 22, 23, 23, 29, 33, 33]
comfort_count(26, may_2022)
comfort_count(27, may_2023)


def comfort_count(temperatures):
    count = 0
    for temp in temperatures:
        if 22 <= temp <= 26:
            count += 1
    return count


nice_days = comfort_count(may_2022)
print('Количество тёплых дней в этом месяце', nice_days)


def is_even():
    number = int(input('Введите число: '))
    result = number
    print(result)
    if (number % 2 == 0):
        print("Число чётное")
    else:
        print("Число не чётное")


is_even()


def calculate_average():
    number = [150, 27, 123, 12, 23]
    print(sum(number) // 2)


calculate_average()

list = [10, 20, 30, 40, 50]


def calculate_sum(list_numbers):
    print(sum(list_numbers))


calculate_sum(list)

numbers1 = [30, 40, 50, 20, 90]
calculate_sum(numbers1)
