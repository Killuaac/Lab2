def lim_max(nums, limit):
    i = len(nums)
    sort_nums = ()
    if i <= 0:                          #в случае отсутствия в кортеже чисел возвращает пояснение
        return("нет соответствующих значений")
    for i in range(nums):
        if nums[i] <= limit:            #сравнивает каждое значение кортежа по индексу и записывает в отдельные кортеж если оно прроходит по условию задачи
            sort_nums = (nums[i], )
        nums[i + 1]
nums = (100, 1, 50, 90, 2)
limit = input
print(lim_max)