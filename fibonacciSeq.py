def fibo(n):
    """
    calculates fibonacci sequence using for loop
    fibo = (n-1) + (n-2)
    returns a list of fibonacci numbers (to the n-th number)
    
    keyword args:
    n -- number of the last element of fibo sequence we want to calculate
    """
    nums = []
    for i in range(n):
        if i == 0:
            nums.append(0)
        elif i == 1: 
            nums.append(1)
        else:
            fib = nums[i-2] + nums[i-1]
            nums.append(fib)
    return nums

def fiboRec(n):
    """
    calculates n-th fibonacci number using recursion
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    m = fiboRec(n-2) + fiboRec(n-1)
    return m
    
memory = {0:0, 1:1, 2:1}
def fiboMem(n):
    """
    calculates n-th fibonacci number using recursion and pseudo memory
    """
    if n not in memory:   
        m = fiboMem(n-2) + fiboMem(n-1)
        memory[n] = m
    return memory[n]

print(fibo(10))
print(fiboRec(10))
print(fiboMem(10))
