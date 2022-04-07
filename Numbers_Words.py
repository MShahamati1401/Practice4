def Numbers_words(list):
    words = 0
    flag = False
    for i in list:
        if i == " " and flag == False:
            flag = True
            words += 1
        if i != " ":
            flag = False
    if list[-1] != " ":
        words = words + 1
    return words

list = []

list = input("Please Inter String:")
print(f"Numbers Of Words : {Numbers_words(list)}")
