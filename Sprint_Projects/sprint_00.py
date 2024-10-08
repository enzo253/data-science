my_name = "Enzo Wurtele"

print(my_name)

my_age = 22

print(my_age)

Julia_age = 32

age_diff = Julia_age - my_age

print(age_diff)

if my_age > 21:
    print("your older then 21")

elif my_age >= 21:
    print("you are 21")

else:
    print("your younger then 21")


if my_age > Julia_age:
    print("your older then Julia")

elif my_age >= Julia_age:
    print("you are the same age as Julia")

else:
    print("your younger then Julia")

friend_list = ["Able", "Broseph", "Dalores", "Fredrick", "George", "Julia"]

print(friend_list[0])
print(friend_list[-1])

for item in friend_list:
    print(item)

friend_age = [22,32,43,54,48,21]

for age in friend_age:
    print (age)

print("------")

for age in friend_age:
    if age % 2 == 0 :
        print(age)

print("-----")

i = 0

while i < len(friend_age):
    birth_num = friend_age[i]
    print(birth_num)
    i += 1

print("-----")

list_00 = [12,34,67,87,32,54,60,]

min_number = min(list_00)
max_number = max(list_00)

print(min_number)
print(max_number)

print("-----")

birth_time = [1999, 1995, 2005, 2010, 2007, 2006, 1994, 1996, 1979, 2008]

for times in birth_time:
    age = 2024 - times
    print(age)

customer_list = [
                    {"name": "Bob", "age": 1999},
                    {"name": "Jack", "age": 1995},
                    {"name": "Lisa", "age": 2005},
                    {"name": "Maria", "age": 2010},
                    {"name": "Ben", "age": 2007},
                    {"name": "Emma", "age": 2006},
                    {"name": "Oscar", "age": 1994},
                    {"name": "Amy", "age": 1996},
                    {"name": "Paul", "age": 1979},
                    {"name": "Etta", "age": 2008}
                ]


for customers in customer_list:
    customer_age = 2024 - customers["age"]
    print (customers["name"], "is", customer_age, "years old")

ages = [20, 24, 14, 9, 12, 13, 25, 23, 40, 11]


i = 0
n = len(ages)

for i in range(n):
    for j in range(0, n-i-1):
        if ages[j] < ages[j+1]:
            temp = ages[j]
            ages[j] = ages[j+1]
            ages[j+1] = temp
i += 1

print(ages)

min_age = ages[-1]
max_age = ages[1]

ages.remove(min_age)
ages.remove(max_age)

print (ages)

berlin = [15, 13, 16, 18, 19, 10, 12 ]
munich = [7, 13, 15, 20, 19, 18, 10, 16]

common_ages = []
for num in berlin:
    if num in munich:
        common_ages.append(num)

print(common_ages)

duplicates = [15,13,16,18,19,15,10]


ages_without_duplicates = []
for age in munich:
    if age not in duplicates:
        ages_without_duplicates.append(age)

print(ages_without_duplicates)

name = input("please enter name: ")

if name == "Jost" or name == "jost":
    print('Welcome Jost, have a nice day!')
elif name == "Evelyn" or name == "evelyn":
    print("Welcome Jost, have a nice day!")
else:
    print("you are not welcomed")

get_length = [1,2,3,4,5,6,7]
n = len(get_length)
i = 0

while i != n:
    i += 1

print(i)

while True:
    try:
        input_age = int(input("whats your age: "))
        
        if 18 <= input_age <= 60:
            print("you have entered a valid age")
            break
        
        else:
            print("you havent entered a valid age")

    except ValueError:
        print("invalid input try again")

list_age = [18,22,24,38,57,40,37,55,48,45]

list_without_age = []

for age in list_age:
    if age != input_age:
        list_without_age.append(age)

print(list_without_age)







