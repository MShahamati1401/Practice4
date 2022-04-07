list_num1 = []
list_num2 = []
list_bigger = []
i = 1
bmm = 1
num1 = int(input("Please Inter First Number: "))
num2 = int(input("Please Inter Second Number: "))
if num2 > num1:
    num2, num1 = num1, num2
for i in range(1, num1):
    if num1 % i == 0:
        list_num1.append(i)
    if num2 % i == 0:
        list_num2.append(i)
flag = 1

if len(list_num1) >= len(list_num2):
    count = len(list_num1)
    list_bigger = list_num1.copy()
else:
    count = len(list_num2)
    list_bigger = list_num2.copy()
print(list_bigger)
index = -1
for flag in range(1, len(list_bigger)):
    if list_bigger[index] in list_num1:
        if list_bigger[index] in list_num2:
            bmm = list_bigger[index]
            break
    index += -1
print(f"B.M.M = {bmm}")
print(f"K.M.M = {round(num1*num2/bmm , 2)}")