a = int(input("请输入一个数计算阶乘:"))
sum = 0
factorial = 1
for i in range(1,a+1):
    factorial = factorial*i
    sum += factorial
print("阶乘之和",sum)

