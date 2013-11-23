# -*- coding:utf-8 -*-

fast_wumpuse = 1
slow_wumpuse = 1000
year = 0
while(fast_wumpuse < slow_wumpuse):
    year += 1
    fast_wumpuse *= 2
    fast_wumpuse -= fast_wumpuse * 0.3
    slow_wumpuse *= 2
    slow_wumpuse -= slow_wumpuse * 0.4

print year
print slow_wumpuse
print fast_wumpuse
