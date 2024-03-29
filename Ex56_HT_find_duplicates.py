# WRITE FIND_DUPLICATES FUNCTION HERE #
#initialise output array
# loop through array
# each number add to dict and set the value to count each time the letter is seen.
#loop through dict
# if count > 1
#add to output array
#return output
def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    
    output = []
    for num, count in num_counts.items():
        if count > 1:
            output.append(num)
    
    return output
#######################################




print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

