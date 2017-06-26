#请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print [n*(n+1) for n in range(1,100,2)]
