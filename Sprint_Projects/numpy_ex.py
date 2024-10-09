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

