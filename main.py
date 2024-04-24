from sortedcontainers import SortedList
from bisect import bisect_left, bisect_right
x = [1,2,3,3,3,5, 6]
arr = SortedList(x)

# arr.remove(3)

print(arr)

print(arr.bisect_right(3), arr[arr.bisect_right(3)]) 
# mean to insert the element at index
# to the right most so that we keep the arr sorted.

# for example, this is returning index 5, at index 5 we have 5, we want 
# to put the value at index 4 and move everything by one index.

print(arr.bisect_left(3),arr[arr.bisect_left(3)])
# for example, this is returning index 2, at index 2 we have 3, we want 
# to put the value at index 4 and move everything by one index.

# simplification
# If we want to insert a value already present in the arr
# right: will not be equal to the given value
# left: will be equal to the given value

# WHat happen if the value is not present.

print(arr.bisect_right(4), arr[arr.bisect_right(4)]) 

print(arr.bisect_left(4),arr[arr.bisect_left(4)])

# the value will be the same.
# the current index value will be greater than the given value
# this means that the current index and upwards need to move by one index

# What happen if the value is less than everything

print(arr.bisect_right(0), arr[arr.bisect_right(0)]) 

print(arr.bisect_left(0),arr[arr.bisect_left(0)])

# it will return zero which the same for the following
print(arr.bisect_left(1),arr[arr.bisect_left(1)])

# What happen if the value is more than everything

print(arr.bisect_right(7), "arr[arr.bisect_right(7)]") 

print(arr.bisect_left(7),"arr[arr.bisect_left(7)]")

# it will return length of the array which the same for the following
print(arr.bisect_right(6),"arr[arr.bisect_right(6)]")
