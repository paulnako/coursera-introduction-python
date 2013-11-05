# -*- coding:utf-8 -*-

a = ["green", "blue", "white", "black"]
b = a
c = list(a)
d = c
a[3] = "red"
c[2] = a[1]
b = a[1 : 3]
b[1] = c[2]

print "a = " + str(a)
print "b = " + str(b)
print "c = " + str(c)
print "d = " + str(d)

print "after"

b[0] = 10000
print "b = " + str(b)
print "a = " + str(a)
