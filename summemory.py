# sum of first n numbers
import tracemalloc as tm

# functions
  # solution1
'''
def sumofN(n):
    sum = 0
    for p in range(1,n+1):
        sum=sum+p
    return sum
'''

  #solution2
def sumofN(n):
    return int(n*(n+1))/2


# programs
tm.start()

t = sumofN(80000)


print(t)
print(tm.get_traced_memory())
tm.stop()

