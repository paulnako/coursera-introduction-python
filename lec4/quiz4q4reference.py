a = [49, 27, 101, -10]
b = a
c = list(a)
d = c
a[3] = 68
c[2] = a[1]
b = a[1 : 3]
b[1] = c[2]

print b
