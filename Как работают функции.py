# def assistant_1():
#     print("Кофе")
#
#
# def assistant_2():
#     i = None
#     while i != "Конец рабочего дня":
#         i = input("Имя звонящего: ")
#         print(i)
#
#
# def assistant_3():
#     assistant_recording = []
#
#     while True:
#         i = input("Имя звонящего: ")
#         if i == "Конец рабочего дня":
#             break
#         assistant_recording.append(i)
#
#     return assistant_recording
#
#
# def assistant_4():
#     print("Кофе")
#     assistant_recording = []
#
#     while True:
#         i = input("Имя звонящего: ")
#         if i == "Конец рабочего дня":
#             break
#         assistant_recording.append(i)
#
#     assistant_recording.sort()
#
#     return assistant_recording
#
#
# # my_recording = assistant_3()
#
#
# def assistant_5(list_recall):
#     for name in list_recall:
#         print("Перезвонил клиенту по имени", name)
#
#
# def assistant_6(list_recall):
#     customer_answers = []
#     for name in list_recall:
#         print("Перезвонил клиенту по имени", name)
#         if input() == "Да":
#             customer_answers.append(True)
#         else:
#             customer_answers.append(False)
#     return customer_answers
#
#
# # my_orders = assistant_6(my_recording)
#
#
# def assistant_7(list_customers, list_orders):
#     for i in range(len(list_customers)+1):
#         if list_orders[i] == True:
#             print(f"Договор заключен с {list_customers[i]}")
#         else:
#             print(f"Договора с {list_customers[i]} не будет, отказ")

