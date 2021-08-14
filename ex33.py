# while循环
def fun(end, step=1):
    i = 0
    numbers = []

    while i < end:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


fun(6, 2)
