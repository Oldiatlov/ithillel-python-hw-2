price = float(input("Введіть ціну: "))
discount_percent = float(input("Введіть знижку (%): "))
percent_to_pay = (100 - discount_percent) / 100
final_price = price * percent_to_pay
print(f"Ціна зі знижкою: {final_price}")