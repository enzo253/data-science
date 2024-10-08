input_array = input("Please input array here: ").split(",")

array_00 = []
for num in input_array:
    array_00.append(int(num.strip()))

print("Input Array:", array_00)


mean = sum(array_00) / len(array_00)

def find_std_dev():
    if len(array_00) <= 1:
        return None  


    total_of_squares = sum((num - mean) ** 2 for num in array_00)

    variance = total_of_squares / len(array_00)

    if len(array_00) % 2 == 0 :
        number = len(array_00) / 2
        fin_num = array_00[number] + array_00[number+2] / 2
        print(f'Median{fin_num}')

    else: 
        number_01 = len(array_00) / 2
        fin_num_01 = array_00[number_01] / 2
        print(f'Median{fin_num_01}')


    
    std_dev = variance ** 0.5

    return mean, variance, median, std_dev



results = find_std_dev()

if results:
    mean, variance, median, std_dev = results
    print(f"Mean: {mean}")
    print(f'Median {median}')
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")
else:
    print("Not enough data to calculate statistics.")
