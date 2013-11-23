# -*- coding:utf-8 -*-

numbers = range(2, 1000)
results = []

while(len(numbers)):
    n = numbers[0]
    results.append(n)
    numbers = filter( lambda x: x % n != 0, numbers )

print len(results)
print results
