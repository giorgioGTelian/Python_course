 data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]
#your code goes here
data.sort()

data.remove(max(data))
data.remove(max(data))
data.remove(min(data))
print(data)

print(sum(data))

📚📚📚👇 REVIEW lists & slices 😉

ℹ Add item at the end
    L.append(x)
    L[len(L):] = [x]

ℹ 	Remove all items
    L.clear()
    del L[:]

ℹ Make a soft copy
    L.copy()
    L[:]

ℹ Return number of items with specified value
    L.count(x)

ℹ	Add items of a list (or any iterable), at the end
    L.extend(iter)
    L[len(L):] = iter

ℹ Return index of first item with specified value. 😲 ValueError if not exist
    L.index(x, start, end)

ℹ	Add item at specified index. -i ⚌ from end 
    L.insert(i, x)

ℹ	Remove item at specified index (or last item if not provided)
    L.pop(i)

ℹ	Remove first item with the specified value. 😲 ValueError if not exist
    L.remove(x)

ℹ	Reverse the order
    L.reverse()
    L[::-1]

ℹ	Sorts the list
    L.sort(*)

ℹ Size of list/iterable
    len(L)

ℹ Min value of number list
    min(L)

ℹ Max value of number list
    max(L)

ℹ Sumatory of number list items
    sum(L)

More on:
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

