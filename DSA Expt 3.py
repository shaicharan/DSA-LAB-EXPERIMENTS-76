import array
# Array creation
arr=array.array('i',[1,2,3])
print(arr)
# Appended a new item 4 at the end of the array
arr.append(4)
print(arr)
# inserted new element 5 at 2nd index position
arr.insert(2,5)
print(arr)
# removed the element at the end of the array
arr.pop()
print(arr)
# removed the item mentioned ar argument
arr.remove(2)
print(arr)
# Return the index position of the value mentioned as argument
print(arr.index(3))
# 5 is at index position 1
print(arr.index(5))
# used to reverse my array
arr.reverse()
print(arr)
