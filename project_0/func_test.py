def number_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_v=1
    max_v=100
    while True:
        count += 1
        predict_number = (min_v+max_v)//2  # предполагаемое число
        print(predict_number)
        if number == predict_number:
            break  # выход из цикла если угадали
        else: 
            
            if predict_number > number:
            #if predict_number-number==3
                max_v = predict_number-1
            else:
                min_v=predict_number+1
        
    return count
print(number_predict(71))
