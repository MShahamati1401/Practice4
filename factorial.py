import math
import time


get_number = int(input("Please Inter Number: "))
time_start = time.time()
h=1
flag = False
get_number_temp = math.floor(get_number ** 0.5)
for i in range(1, get_number_temp):
    h *= i
    if h == get_number:
        print("YES")
        flag = True
        break
if flag == False:
    print("NO")
timp_end = time.time()
time_real = timp_end - time_start
print(time_real)