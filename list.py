"""
python list is an array in python

python list can store values with different datatype in same list

syntax=> list name = [ , , ]

tuple===> list name = ( , , )
** tuple cannot be modified in python (immutable)
** list can be modified (mutable)
"""

list1 = ["apple", "boy", "cat", "dog", 1, 2, 3, 4, 5.6, 5.7, 8.9, 10.0]

print(list1)

# pop remove last element of list and returns that element
print(list1.pop())
# now 10.0 is removed from the list

# slicing in list   (same as string slicing)
print(list1[2:5])
print(list1[::])
print(list1[::-1])

# list functions
"""
list.sort() ==> sort list to increasing order order
list.append() ==> add element at end of list
list.clear() ==> remove all elements from list
list.copy() ==> returns copy of the list
list.insert() ==> add element with specified location
list.remove() ==> remove element from specified location
list.count() ==> returns number of element with specified value
list.index() ==> returns index of element with specified value
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print()
print(nums)
print(nums[1])  # returns element with index 1
print("number of 10 coming is", nums.count(10))  # there is no 10 in list so return 0

nums.append(10)
nums.append(10)
nums.append(10)
# 10 is added 3 times in the list

print(nums)
print("number of 10 coming is", nums.count(10))  # now there is 3 10

nums.sort()  # sorts list so 0 comes first
print(nums)

nums.remove(10)
temp = nums.pop()  # removes element with value of 10 two times
print(nums, temp)  # also returns 10 from pop stored in temp

nums.append(321)
print(nums)
print(nums.index(321))  # returns index of 321
print(nums.copy())  # returns copy of list

"""
tuple===>

tuple is immutable list on python

values of tuple cannot be changed, it is a constant list
"""
tp = (1, 3, 6, 8)
print()
print(tp)
print(tp[1])
# tp[3] = 23 will give error
# modification in tuple is not allowed
