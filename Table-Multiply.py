
def multi(x, y):
    for i in range(1, num1 + 1):
        for j in range(1, num2 + 1):
            print(f"{j} * {i} = ", i * j, end="     ")
        print()
    return

num1 = int(input("Please Inter First Number: "))
num2 = int(input("Please Inter Second Number: "))
multi(num1, num2)