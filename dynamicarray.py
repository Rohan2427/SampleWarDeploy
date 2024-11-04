import sys #importing related module for fetching the bytes occupied

H = []  # Initiating a blank array


for d in range(0,100):         #Initiating for loop from 0 to 99
  print(d, sys.getsizeof(H))   #printing the byte size occupied by this array.
  H.append(d)                  #Infusing the values in the array, initiating from zero to 99.
