import random
import logging

logging.basicConfig(filename="lab10.log", level=logging.DEBUG, format ="%(asctime)s %(levelname)s %(message)s" )

logging.info("Начался ввод количества бочек")
while True:  # Проверка ввода
    try:
        n = int(input("Введите количество бочек (целое число): "))
        if  n<1:  #проверка положительное ли число бочек
            logging.error("Ошибка некорректного ввода")
            print("Количество бочек должно быть положительным числом")
        else:
            break
    except ValueError:
        logging.error("Ошибка некорректного ввода")
        print("Некорректный ввод")
        pass

digits=list(range(1, n+1)) #создала список n чисел

random.shuffle(digits) #перемешала эти числа

logging.info("Начался вывод чисел")

for i in range(n): #вывод этих чисел
    k=input("Нажмите любую клавишу чтобы получить случайное число")
    print("Число", digits[i])
logging.info("Вывод чисел закончился")
x = input("Нажмите любую клавишу чтобы завершить программу")
logging.info("Программа завершилась")
