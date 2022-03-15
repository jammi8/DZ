name = "Джамиля"
print(name, "\n")

age = 19
print("Мне", age, "лет.\n")

nameRepeat = name * 5
print(nameRepeat, "\n")

namedif = input("Введите своё имя: ")
agedif = input("Введите свой возраст: ")
c = 0
if namedif.count(" ") == 0 and 0 <= int(agedif) <= 150:
    print("Привет,", namedif, "! Не может быть, что Вам уже", agedif, ".\n")
else:
    print("Данные введены неправильно!")
    c = -1

a = int(agedif)
if c != -1:
    if a <= 13:
        print("Вам", a, "? Вы так молоды!\n")
    elif 13 < a <= 17:
        print("Вам", a, "? Так вы подросток!\n")
    elif 17 < a <= 25:
        print("Вам", a, "? Как взрослая жизнь?\n")
    elif a > 25:
        print("Вам", a, "? Надеюсь у Вас всё хорошо :-)\n")

if c != -1:
    w1 = namedif[1:-1:]
    w2 = namedif[::-1]
    w3 = namedif[-3:]
    w4 = namedif[:5]
    print(w1, w2, w3, w4, "\n")

summa = 0
mult = 1
if c != -1:
    while a > 0:
        d = a % 10
        summa += d
        mult *= d
        a = a // 10
    print("Количество символов в имени: ", len(namedif))
    print("Сумма чисел: ", summa)
    print("Произведение чисел: ", mult, "\n")

if c != -1:
    p = namedif.capitalize()
    print(namedif.upper(), namedif.lower(), p, p.swapcase(), "\n")

print("Сколько будет 5*3+8?")
n = input("Ответ: ")
t = int(n)
if t == 5 * 3 + 8:
    print("Правильный ответ!")
else:
    print("Неправильный ответ.")
