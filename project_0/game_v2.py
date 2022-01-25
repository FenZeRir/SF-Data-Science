'''Игра угадай число
Компьютер загадывает и угадывает за минимальное колличество попыток'''

from random import randint
import numpy as np

def random_predict(number:int=1) -> int:
    """Загадываем рандом число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number =  np.random.randint(1, 101)#предполагаемое число
        if number == predict_number:
            break #выход из цикла если угадали
    return(count)    

def score_game(random_predict) -> int:
    """за какое колличество попыток алгоритм в среднем угадает(1000 подходов)
    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: среднее колличество попыток
    """
    count_ls = []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))#загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывал в среднем за {score} попыток')
    return(score)