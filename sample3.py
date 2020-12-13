
from array import *

array_num = array('i', [1,3,5,7,9,3])

#2 : append a new item to the end of the array
array_num.append(11)

print('===' * 100)

#1 : display the array items.
for i in array_num:
    print(i)

print('===' * 100)
#3 : reverse the order of the items
print(array_num[::-1])

print('===' * 100)
#4 :  Get the length in bytes of one array item
print(array_num.itemsize)

print('===' * 100)

#5
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
print(len(array_num) * array_num.itemsize)

print('===' * 100)
#6
def countX(lst, x):
    count = 0

    for i in lst:
        if i == x:
            count += 1
    return count
lst = [1,3,5,3,9,3,7,2]
x = 3

print(countX(lst, x))

print('===' * 100)

#6.1.

print(array_num.count(3))

print('===' * 100)
#7. append items from inerrable to the end of the array.

array_num.extend(array_num)
print(array_num)
lst.extend(lst)
print(lst)

#8.

x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
s = x.tobytes()
print(s)


#9.












