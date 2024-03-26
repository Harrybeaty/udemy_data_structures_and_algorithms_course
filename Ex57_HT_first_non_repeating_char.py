# WRITE THE FUNCTION HERE #
# create dict
# iterate through string
# add to dict key, value is a counter

#loop through dict
# if count = 1
#   print key

#return None
def first_non_repeating_char(string):
    letter_counts = {}
    for letter in string:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    for letter, count in letter_counts.items():
        if count == 1:
            return letter
    return None
###########################



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""