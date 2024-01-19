class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # WRITE THE PRINT_LIST METHOD HERE #
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)          # Create the new node.
        if self.head is None:           # If the list is empty aka, head doesn't point to anything.
            self.head = new_node        # set head to point to the new node.
            self.tail = new_node        # set tail to point to the new node.
        else:                           # If list is not empty.
            self.tail.next = new_node   # This is making the last element now point to the new element. 
            self.tail = new_node        # Set tail to point at the new_node
        self.length += 1                # Increase length by 1
        return True                     # this is optional but it will be needed fo another method later.
    
    def pop(self):
        if self.head is None:           # If there are no nodes.
            return None                 
        temp = self.head                # Temp is used to iterate through the list ahead of pre.
        pre = self.head                 # pre is used to iterate through the list and it allows us to find the second last node when temp reaches the end.
        while(temp.next is not None):   # This loop will run until temp gets to the end of the list.
            pre = temp                  # pre to temp
            temp = temp.next            # temp moves up one.
        self.tail = pre                 # Once the end is found temp is on the last element and pre is on the second last. so set tail to pre.
        self.tail.next = None           # Set the next of the last element to None.
        self.length -= 1                # Reduce the length.
        if self.length == 0:            # This is the edge case for if we have one node. when we have one node we still run some of the code above.
            self.head = None            
            self.tail = None            # We don't need to change the length because the code above has already done that.
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:           # Edge case if there is nothing in the LL.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head   # Set new node to point at the original first node by setting it to head.
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.head == None:           
            return None
        temp = self.head                # create temp and set it to the element you wnat to remove.
        self.head = self.head.next      # set head to point and the 2nd element in the list.
        temp.next = None                # isolate the removed item
        self.length -= 1                # reduce the length
        if self.length == 0:            # edge case for when list has 1 element, remember length has already been decreased. 
            self.tail = None            # nothing in list, so set tail to non, head is already pointing to none in this case.
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):      # _ should be used when you don't use the iterator in the loop.
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
       temp = self.get(index)       # Used to check index is withing the length and find the node to set a value.
       if temp is not None:         # .get method returns either None or a node
           temp.value = value       # Set the value to new value.
           return True              
       return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value) # code for this case has already been written
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)     # This makes temp point at the node before index.
        new_node.next = temp.next      # This points our ne node at the node that needs to be after it.
        temp.next = new_node           # This makes the node before the new node point to the new node.
        self.length += 1
        return True