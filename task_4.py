def temp_cat(temp):
    if temp < - 20:                      #Программа принимает значение и сравнивает их с заданными ранжировками
        return 'Ответ = 0 # Холодно'
    elif temp in range(-20: 0):
        return 'Ответ = 1 # Прохладно'
    elif temp in range(0.1: 15):
        return 'Ответ = 2 # Зябко'
    elif temp in range(15.1: 25):
        return 'Ответ = 3 # Тепло'
    elif temp > 25:
        return 'Ответ = 4 # Жарко'
print(temp_cat(float(input())))

