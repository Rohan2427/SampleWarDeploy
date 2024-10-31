# sum of first n numbers

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

t = sumofN(8)
print(t)


