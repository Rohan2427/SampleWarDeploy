def sum_digits(num):

    sum = 0
    while (num> 0):
        sum+=num%10
        num/=10

    return sum

sum_digits(12345678)
