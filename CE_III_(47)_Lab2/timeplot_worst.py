from insertionSort import insertion_sort
from mergeSort import merge_sort
import time
import random
import matplotlib.pyplot as plt 

l = 1000
n, t1, t2 = [], [], []
for j in range(l, l*10, l):
    A = [int(random.random()*l) for i in range(j)]
    start = time.time()
    d = insertion_sort(A)
    end = time.time()
    b = end - start
    t1.append(b)
    n.append(j)

    Z = [int(random.random()*l) for i in range(j)]
    start = time.time()
    d = merge_sort(A)
    end = time.time()
    b = end - start
    t2.append(b)
    # n.append(j)

# print(n, t1)
plt.plot(n,t1, label='insertion_sort')
plt.plot(n,t2, label='merge_sort')
plt.title('Worst Case')
plt.xlabel('Input size(n)')
plt.ylabel('Execution time(t)')
plt.legend()
plt.show()