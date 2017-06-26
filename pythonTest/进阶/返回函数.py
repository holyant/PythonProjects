def calc_prod(lst):
    def product():
        re=1
        for v in lst:
            re = re*v
        return re;
    return product

f = calc_prod([1, 2, 3, 4])
print f()
