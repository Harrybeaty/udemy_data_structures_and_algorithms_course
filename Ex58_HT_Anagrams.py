# WRITE GROUP_ANAGRAMS FUNCTION HERE #
# init dict
# loop through strings
# sort each letter in string to alphabetical order
# if in dict
# add string to the value of canonical key
def group_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagrams:
            anagrams[canonical].append(string)
        else:
            anagrams[canonical] = [string]
    return list(anagrams.values())
######################################




print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""