#Быстрая сортировка
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Выбираем средний элемент как опорный
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

numbers = [3,6,8,-10,4,3,-9,-3,10,1,2,1]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)

#Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две части
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Сливаем отсортированные части
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0
    # Сравниваем элементы и добавляем в результат
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Пример использования
numbers = [3,6,8,-10,4,3,-9,-3,10,1,2,1]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)