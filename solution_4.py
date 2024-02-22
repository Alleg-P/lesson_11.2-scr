# Задача 4: Перевод единиц измерения

def convert_units_with_while(values, unit):
    i = 0
    while i < len(values):
        if unit == 'meters':
            converted_value = values[i] * 3.28084
            print(f"{values[i]} meter(s) = {converted_value} foot(feet)")
            i += 1

values = [1, 2]
unit = 'meters'
convert_units_with_while(values, unit)
