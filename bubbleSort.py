# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:11:25 2018

@author: MCA

Bubble sort example.
"""

def bubble(m):
    for i in range(len(m)-1, 0,-1):
        print (m)
        for j in range(i):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
    return m


a = [5,33,2,5,6,0,11]
print (bubble(a))