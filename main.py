# def zad1(number):
#     return number % 3 == 0
# number = int(input("Введите число "))
# print(zad1(number))

def zadacha2():
    def num2(chislo):
        return 100 / chislo
    try:
        chislo = int(input("Введите число "))
        print(num2(chislo))
    except ValueError:
        print("Это не число")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
zadacha2()
