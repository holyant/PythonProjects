def average(*args):
    sum =0
    if len(args)==0:
        return 0
    for arg in args:
       sum+=arg
    return float(sum)/len(args)

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)
