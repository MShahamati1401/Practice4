a = "*"
b = "#"
num1 = int(input("Please rows: "))
num2 = int(input("Please columns: "))
for i in range(num1):
    for j in range(num2 // 2):
        print(a+b, end="")
    if num2 % 2 != 0:
        print(a, end="")
    a, b = b, a
    print()