
input_list_check = input("input ages here: ").split(",")

list_check = []

for num in input_list_check:
    list_check.append(int(num))

print(list_check)

check = int(input("check a age for duplicates: "))

list_only_num = []
list_only_num.append(check)
print(check)

final_check = []

count = list_check.count(check)

if count > 1:
    print(f'this number is a duplicate here is the amount of times it has been found repeating',{count2})

else:
    print("this number is not duplicated")


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


        




