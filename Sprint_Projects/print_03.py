input_array = input("Please input array here: ").split(",")

array_00 = []
for num in input_array:
    array_00.append(int(num.strip()))

print("Input Array:", array_00)


def find_std_dev():
    if len(array_00) <= 1:
        return None

    mean = sum(array_00) / len(array_00)

    total_of_squares = sum((num - mean) ** 2 for num in array_00)

    variance = total_of_squares / len(array_00)

    array_00.sort()

    if len(array_00) % 2 == 0 :
        mid_index = len(array_00) // 2
        median = array_00[mid_index] + array_00[mid_index - 1] / 2

    else: 
        mid_index = len(array_00) // 2  
        median = array_00[mid_index]


    
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


#Sprint 02

#Ex _02 = increase
#Ex_03 = E
#Ex_04 = 10
#Ex_05 = skewed left
#Ex_06 = 15,000
#Ex_07 = 35,000
#Ex_08 = D
#Ex_09 = Standard Deviation: 10.44030650891055
#Ex_10 = B
#Ex_11 = D