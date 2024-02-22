# Задача 3: Отслеживание запасов

def track_low_stock_with_for(products, threshold):
    print("Низкий запас:")
    for product, quantity in products.items():
        if quantity < threshold:
            print(f"{product} - {quantity}")

track_low_stock_with_for({'apples': 50, 'bananas': 10, 'cherries': 3}, 15)
