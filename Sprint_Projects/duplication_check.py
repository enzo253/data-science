
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
    print(f'this number is a duplicate here is the amount of times it has been found repeating',{count})

else:
    print("this number is not duplicated")



        




