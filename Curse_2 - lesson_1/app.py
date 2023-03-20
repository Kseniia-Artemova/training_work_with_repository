from validators.validate_pin import validate_pin
from validators.validate_card import validate_card

print("Введите ваш номер карты")
card_number = input()
print("Введите ваш ПИН-код")
card_pin = input()

print("Номер карты допустимый" if validate_card(card_number) else "Номер карты недопустимый")
print("ПИН-код допустимый" if validate_pin(card_pin) else "ПИН-код недопустимый")