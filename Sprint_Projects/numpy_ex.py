import numpy as np

arr = np.arange(1,10)

print(arr)

arr = np.random.randint(1,10, size = (3,3))

print(arr)

arr = np.array([1,2,3,4,5,6,7,8,9,10])

arr = np.random.randint(1,10, size=(3,3))

sum_num = sum(arr)

mean = np.mean(arr)

std_dev = np.std(arr)

print(sum_num)

print(mean)

print(std_dev)

element = arr[1,2]

print(element)

arr = np.array([10,9,8,7,6,5,4,3,2,1])

arr_1 = np.array([1,2,3,4,5,6,7,8,9,10])

add = arr + arr_1

multy = arr * arr_1

devide = arr / arr_1

sub = arr_1 - arr 

print(f'\n{add}\n{multy}\n{devide}\n{sub}')

print(add)

arr = np.random.randint(1,10, size=(4,4))

print(arr)

element = arr[:2, :3]

print(f'\n{element}')

arr = np.random.randint(1,100, size=(20))

print("\n",arr)

count = np.sum(arr >= 25)
print(count)

arr = np.random.randint(1,100, size=(3,4))

value_1 = sum(arr[0:])

value_2 = np.sum(arr, axis=1)

print(arr)

print(value_1, value_2)

min_num = np.min(arr)

max_num = np.max(arr)

print(min_num, max_num)

arr = np.arange(12)

arr = arr.reshape(3,4)

arr = arr.reshape(-1)

print(arr)

x1 = np.random.normal(loc = 0, scale = 1, size = 100)

x2 = np.random.uniform(low = 0, high = 1, size = 100)

correlation_matrix = np.corrcoef(x1,x2)

correlation_coefficent = correlation_matrix[0,1]

dataset = np.column_stack((x1, x2))

elements = dataset[:5]

print(elements)

print(correlation_coefficent)

arr_02 = np.random.randint(0,50, size=(10,2))

np.savetxt("arr_02.csv", arr_02, delimiter=',', header='x1,x2', comments='')

loaded_arr = np.loadtxt('arr_02.csv', delimiter=',', skiprows=1)

print(loaded_arr)



