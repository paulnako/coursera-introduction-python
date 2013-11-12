# -*- coding:utf-8 -*-

ll = [0, 1]

for i in range(1, 41):
    ll.append(ll[i-1] + ll[i])

print ll[len(ll) - 1]
