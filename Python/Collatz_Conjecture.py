def check_num(num):
    iterations = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            iterations += 1
        else:
            num = 3 * num + 1
            iterations += 1
    print(f"The number of iterations to reach {int(num)} is {iterations} ")


n = int(input("Enter a positive integer: "))
check_num(n)
