# WRITE ITEM_IN_COMMON FUNCTION HERE #
def item_in_common(list1, list2):
    diction = {}
    for i in list1:
        diction[i] = True
    
    for j in list2:
        if j in diction:
            return True
    
    return False
        
######################################




list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""