# Задача 2: Подсчет определенных товаров

def count_specific_items_with_while(items, target):
    count = 0
    index = 0
    while index < len(items):
        if items[index] == target:
            count += 1
        index += 1
    return count

items1 = ['fruit', 'toy', 'fruit', 'toy']
target1 = 'toy'
print(f"Количество '{target1}': {count_specific_items_with_while(items1, target1)}")

items2 = ['clothes', 'clothes', 'clothes']
target2 = 'clothes'
print(f"Количество '{target2}': {count_specific_items_with_while(items2, target2)}")
