import itertools
import operator

### 1. Infinite Iterators ###
print("Infinite Iterators:")

# count(start, step)
print("Count (1 to 10, step=2):")
for number in itertools.count(1, 2):
    if number > 10:
        break
    print(number, end=" ")
print("\n")

# cycle(iterable)
print("Cycle ('AB' 8 times):")
counter = 0
for char in itertools.cycle("AB"):
    if counter > 7:
        break
    print(char, end=" ")
    counter += 1
print("\n")

# repeat(val, num)
print("Repeat 25 four times:")
print(list(itertools.repeat(25, 4)))
print("\n")


### 2. Combinatoric Iterators ###
print("Combinatoric Iterators:")

# product(*iterables, repeat=n)
print("Cartesian Product of [1,2] repeated 2 times:")
print(list(itertools.product([1, 2], repeat=2)))
print("\n")

# permutations(iterable, r)
print("Permutations of 'AB' (r=2):")
print(list(itertools.permutations("AB", 2)))
print("\n")

# combinations(iterable, r)
print("Combinations of 'AB' (r=2):")
print(list(itertools.combinations("AB", 2)))
print("\n")

# combinations_with_replacement(iterable, r)
print("Combinations with Replacement of 'AB' (r=2):")
print(list(itertools.combinations_with_replacement("AB", 2)))
print("\n")


### 3. Terminating Iterators ###
print("Terminating Iterators:")

# accumulate(iterable, func)
print("Accumulate multiplication on [1, 4, 5]:")
nums = [1, 4, 5]
print(list(itertools.accumulate(nums, operator.mul)))
print("\n")

# chain(*iterables)
print("Chaining 'AB' and [1, 2]:")
print(list(itertools.chain("AB", [1, 2])))
print("\n")

# compress(data, selectors)
print("Compress 'ABCDEF' with [1,0,1,0,1,0]:")
print(list(itertools.compress("ABCDEF", [1, 0, 1, 0, 1, 0])))
print("\n")

# dropwhile(func, iterable)
print("Drop while x < 3 in [1, 2, 3, 4, 5]:")
print(list(itertools.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5])))
print("\n")

# filterfalse(func, iterable)
print("Filter false (keep odd numbers) from [1, 2, 3, 4]:")
print(list(itertools.filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4])))
print("\n")

# islice(iterable, start, stop, step)
print("Slice [0,1,2,3,4] from index 1 to 4, step 2:")
print(list(itertools.islice([0, 1, 2, 3, 4], 1, 4, 2)))
print("\n")

# tee(iterable, n)
print("Tee iterator duplication:")
nums = iter([1, 2, 3])
iter1, iter2 = itertools.tee(nums, 2)
print(list(iter1), list(iter2))
print("\n")

# zip_longest(*iterables, fillvalue)
print("Zip longest 'AB' and '123' with fillvalue '?':")
print(list(itertools.zip_longest("AB", "123", fillvalue="?")))
print("\n")
