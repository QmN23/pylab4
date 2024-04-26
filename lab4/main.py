# Task 1
# def count_unique_numbers(n):
#     unique_numbers = set(numbers)
#     return len(unique_numbers)
#
#
# inputs = [[1, 5, 3, 6, 4, 7, 2, 5, 6, 7, 3, 3, 5, 6, 3, 2, 2, 5]]
#
# for numbers in inputs:
#     unique_count = count_unique_numbers(numbers)
#     print(f"Входные данные: {inputs}.")
#     print(f"Выходные значения: {unique_count}.")

# Task 2
# def is_subset(set1, set2):
#     for item in set1:
#         if item not in set2:
#             return False
#     if set1 == set2:
#         return False
#     return True
#
#
# inputs = [
#     ({1, 2, 3}, {1, 4, 5}),
#     ({1, 2, 3, 4, 5, 6, 7}, {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}),
#     ({1, 10, 223, 413, 2}, {1, 10, 223, 413, 2})
# ]
#
# for set1, set2 in inputs:
#     print(f"Входные данные: {set1} и {set2}.")
#     print(f"Выходные значения: {is_subset(set1, set2)}.")

# Task 3
# cities_set = set()
#
# while True:
#     city = input("Напишите город: ")
#
#     if city in cities_set:
#         print("REPEAT")
#     else:
#         cities_set.add(city)
#         print("OK")


# Task 4

# def count(text):
#     words = text.split()
#     word_count = {}
#     result = []
#
#     for word in words:
#         if word in word_count:
#             result.append(word_count[word])
#         else:
#             result.append(0)
#         word_count[word] = word_count.get(word, 0) + 1
#
#     return result
#
#
# string = "one two one two three"
# output = count(string)
# print("Входная строка:", string)
# print("Вывод:", output)

# Task 5
# def count_items_purchased(n):
#     purchases = {}
#
#     for i in range(n):
#         record = input("Введите запись о покупке (ID покупателя Товар Количество): ").split()
#         buyer_id, item, count = int(record[0]), record[1], int(record[2])
#
#         if buyer_id not in purchases:
#             purchases[buyer_id] = []
#
#         purchases[buyer_id].append((item, count))
#
#     for buyer_id, purchase_list in purchases.items():
#         print(f"{buyer_id}:")
#         for item, count in purchase_list:
#             print(f"{item} {count}")
#
#
# count_items_purchased(int(input("Введите количество записей о покупках: ")))


# Task 6
def sort_words(text):
    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))  # -x[1] для сортировки по убыванию, x[0]
    # для лексикографического

    for word, count in sorted_words:
        print(word)


input_text = input()
print("Результат:")
sort_words(input_text)
