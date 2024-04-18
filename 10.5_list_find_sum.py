def esercizio(nums, ref):
    for index1 in range(len(nums)):
        for index2 in range(index1 + 1, len(nums)):
            if nums[index1] + nums[index2] == ref:
                return (index1, index2)
    return None

res = esercizio([3, 7, 11, 25], 10)
print(res)
res = esercizio([1, 2, 3, 2], 4)
print(res)
res = esercizio([1, 5, 3, 2], 9)
print(res)
