x = [1,2,3]
y0 = lambda x:x*2
y1 = lambda **kwargs: 1
y2 = lambda *args: sum(args)
print(y2(1,2))
print(y0(x))