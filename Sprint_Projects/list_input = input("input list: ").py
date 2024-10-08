list_input = input("input list: ").split(",")

list_with_duplicates = []

for num in list_input:
    list_with_duplicates.append(int(num))

print(list_with_duplicates)

list_without_duplicates = []

for num in list_with_duplicates:
    if num not in list_without_duplicates:
        list_without_duplicates.append(num)

print(list_without_duplicates)
print("--------")