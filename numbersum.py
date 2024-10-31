# sum of first n numbers
from time import time

# functions
  # solution1

def sumofN(n):
    sum = 0
    for p in range(1,n+1):
        sum=sum+p
    return sum

'''
  #solution2
def sumofN(n):
    return int(n*(n+1))/2
'''

# programs

s_time=time()
t = sumofN(8888888)
e_time=time()
d_time=e_time-s_time
print(t)
print(d_time)


