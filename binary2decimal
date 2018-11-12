def bin2decStr(num):
    """
    function uses string parsing and then iterates through the number byte by byte
    while calculating the decimal value
    """
    n = list(str(num))
    sum_ = 0
    length = len(n)
    i = 0
    j = 0
    for i in reversed(range(length)):
        sum_ = sum_  + int(n[j])*(2**i)
        j+=1
    return sum_

def bin2dec(num):
    """
    function uses modulus arithmetic 
    to calculate the decimal value
    """
    i = 0
    sum_ = 0
    while num>0:
        mod = num%10
        num = num//10
        sum_ += mod*2**i
        i += 1
    return sum_


import time

start = time.clock()
print(bin2dec(1000001101111111111111111111110000110010))
end = time.clock()
print(end-start)

start = time.clock()
print(bin2decStr(1000001101111111111111111111110000110010))
end = time.clock()
print(end-start)
