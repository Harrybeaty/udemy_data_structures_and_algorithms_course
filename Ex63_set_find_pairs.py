# WRITE FIND_PAIRS FUNCTION HERE #
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)                    # Use set because if there were dupes in the array it would put 2 pairs in the output when it should be one.
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs
##################################




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""