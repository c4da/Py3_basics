# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:56:17 2018

@author: MCA

function prints pascalls triangle to the n-th row
"""

def pascal(n):
    
    def one(m):
        return m.append(1)
    
    lines = []
    for j in range(n):
        line = []
        if j == 0:
            one(line)
        elif j == 1:
            one(line)
            one(line)
            
        else:
            one(line)
            for i in range(j-1):
                line.append(lines[j-1][i]+lines[j-1][i+1])
            one(line)
            
        lines.append(line)
        
    return lines
            
print (pascal(5))