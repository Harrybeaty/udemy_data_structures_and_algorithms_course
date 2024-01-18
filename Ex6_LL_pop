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
