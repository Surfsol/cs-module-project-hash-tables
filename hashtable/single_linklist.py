class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
#array full of linkedlist
class LinkedList:
    def __init__(self):
        self.head = None
    def find(self, key):
        #want to find match in linked list
        current = self.head

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def insert_head(self, key, value):
        #create node
        # check if key already in linked list
        current = self.head
        # update value
        while current is not None:
          
            if current.key == key:
                current.value = value
                return
            current = current.next
        #if not, make a new node and insert at head
        #HashTableEntry, has next value
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node
        
    def delete(self):   
        pass

#make linked list with hashtable
# put > get index 

#Load_Factor
#count all items / number of slots

#load factor tell us to resize? 
## .7 load factor, resize
## .2 resize down

#resize table

# How to reszie to a larger hashtable
# double size of array
# iterate through old array and old linked list
# insert into new array, will make different index

# make linked list work with hashtable
# resize 