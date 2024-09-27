a = float(input())
discount = 35
discount_z = 0
k = (100 - discount)/100
if a>20:
    fc = a*k
    print(f"Итоговая стоимость: {fc}. Скидка: {discount}%")
else:
    print(f"Итоговая стоимость: {a}. Скидка: {discount_z}%")