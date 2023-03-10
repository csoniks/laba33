"gjgjukjuh"
words =[]
while (nwords := (str(input("введите слово")))) != "stop":
    words.append(nwords)
print(" ".join(words))

def z32():
    words = []
    while True:
        nwords = str(input("Введите слово"))
        if nwords != "stop":
            words.append(nwords)
        else:
            print(" ".join(words))
            break

def z33():
    while (nwords := (str(input("ведите слово")))) != "stop":
        if "ф" in nwords or "Ф" in nwords:
            print("Ого, это очень редкое слово")
        else:
            print("Эх, это не очень редкое слово")

from random import randint
def z34():
    prav = 0
    neprav = 0
    while True:
        x = randint(1, 100)
        y = randint(1, 100)
        print(f"{x} + {y} = ", end="")
        rez = input()
        while not rez.isdigit() and rez != "stop":
            print("ошибка, начни снова: ", end="")
            rez = input()
        if rez == "stop":
            break
        rez = int(rez)
        if x + y == rez:
            prav += 1
            print("правильно")
        if x + y != rez:
            neprav += 1
            print("неправильно")
        if neprav == 3:
            print("игра окончена")
            print("колво правильных ответов: ", prav)
            break
z32()
z33()
z34()