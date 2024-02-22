# Задача 1: Суммирование продаж

def sum_sales_with_for(sales):
    total = 0
    for sale in sales:
        total += sale

    print("Сумма продаж:", end=' ')
    print(*sales, sep='+', end='=')
    print(total)

sales = [100, 200, 300]
sum_sales_with_for(sales)
