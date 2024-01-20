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
