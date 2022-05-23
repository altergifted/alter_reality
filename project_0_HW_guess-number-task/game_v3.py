"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def number_predict(number: int = 1) -> int:
    """Угадываем число по алгоритму африканских охотников

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_v = 1
    max_v = 100
    
    while True:
        count += 1
        predict_number = (min_v+max_v) // 2  # предполагаемое число
        
        if number == predict_number:
            break  # выход из цикла если угадали
        elif predict_number > number:
            max_v = predict_number - 1
        else:
            min_v = predict_number + 1
        
    return count


def score_game(number_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(number_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(number_predict)
