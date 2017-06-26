def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(10)

#由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面
