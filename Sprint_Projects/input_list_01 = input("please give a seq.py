input_list_01 = input("please give a sequence here: ").split(",")

input_list_02 = []

for num in input_list_01:
    input_list_02.append(num)

list_01 =[]
for num in input_list_02:
    if num * 2 == 0:
        list_01.append(num)

list_02 = []
for num in input_list_02:
    if num * 2 == 1:
        list_02.append(num)

if list_02 > list_01:
    print(list_02)

if list_01 > list_02:
    print(list_01)
