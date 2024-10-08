input_list_01 = input("please give a sequence here: ").split(",")

input_list_02 = []

for num in input_list_01:
    input_list_02.append(int(num))

list_02 = []
list_01 = []
for num in input_list_02:
    if num % 2 == 0:
        list_01.append(num)

    else:
        list_02.append(num)

if len(list_02) > len(list_01):
    print(f',{list_02}"the outlier is: "{list_01}')

elif len(list_01) > len(list_02):
    print(f',{list_01}, "the outlier is: ", {list_02}')
