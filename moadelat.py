a_x_2 = int(input("Please Inter zarib X2: "))
b_x = int(input("Please Inter zarib X: "))
c = int(input("Please Inter zarib C: "))
delta = (b_x ** 2) - (4*a_x_2 * c)
print(delta)
if delta == 0:
    print("Javab Moadele : ")
    output = (-(b_x) * (delta ** 1/2)) / (2 * a_x_2)
    print(output)
elif delta > 0:
    print("Javab Moadele : ")
    output = (-(b_x) - (delta ** 0.5)) / (2 * a_x_2)
    output2 = (-(b_x) + (delta ** 0.5)) / (2 * a_x_2)
    print("X1 = ", round(output, 2), "X2 = ", round(output2, 2))
else:
    print("Delta < 0 ERROR")

print("Test : ", a_x_2 * ( output ** 2) + (b_x * output) + c)
print("Test : ", a_x_2 * ( output2 ** 2) + (b_x * output2) + c)