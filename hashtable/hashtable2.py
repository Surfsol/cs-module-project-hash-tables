class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    


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


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
# store original key: value to an index
#put with no collision: add node
#put with collision: add node to head or tail
#get hash key, go to index
 # compare with original key, if key matches return value
 # if not found return None
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        #[none] * capacity
        self.capacity = [None for _ in range(capacity)]
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        
        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        #find number of elements / capacity
        pass

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        #key is string, turn into a number
        
        fnv_prime = 1099511628211
        hash = 14695981039346656037
        for i in key:
            hash = hash * fnv_prime
            #Bitwise XOR ^
            hash = hash ^ ord(i)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        #for byte in key:


        #self.djb2 = key*16777619
        pass

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key)%self.get_num_slots()
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # hashed key
        hashedKey = self.hash_index(key)
        # #print('hashedKey', hashedKey)
        # #insert to head
        if self.capacity[hashedKey] == None:
            #enter object in first slot
            self.capacity[hashedKey] = HashTableEntry(key, value)

            
        if self.capacity[hashedKey] != None:
            print('collision', self.capacity[hashedKey])
            #check to see it key exists
            node = self.capacity[hashedKey]
            while node:
                #check to see if key already exists
                if node.key == key:
                    #if does update with value
                    node.value = value
                    return
                #go to next node
                prev = node
                #set node to next
                node = node.next
            #when no more node, put in tail
            prev.next = HashTableEntry(key, value)


        #HashTableEntry(hashedKey , value)
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        keyHash = self.hash_index(key)
        cur = self.capacity[keyHash]
        if cur == None:
            print('warning Key not found')
        # if key is head
        if cur.key == key:
            cur.value = None
            cur = cur.next
            return cur
        else:    # key not head
            while cur != None:
                prev = cur
                #see if keys matchs
                cur = cur.next
                if cur.key == key:
                    #set prev next to cur.next, to skip over current
                    prev.next = cur.next
                    #self.get_load_factor()
                    return cur.value
            
            #set current to next
            
            #otherwise check the next node
            
          
            

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        cur = self.capacity[index]
        #print('index', index, 'self.capacity',self.capacity,'this is currenttttt',cur)
        # if cur.key == key:
        #     return cur.value
        flag = True
        while flag and cur != None:
            if cur.key == key:
                flag = False
                return cur.value  
            cur = cur.next
        return None




      


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # if get_load factor 
        print('lennnthth',len(self.capacity))
        for i in self.capacity:
            print(self.capacity[i])
    

if __name__ == "__main__":
    ht = HashTable(8)

    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    ht.delete("key-7")
    ht.delete("key-6")
    ht.delete("key-5")
    ht.delete("key-4")
    ht.delete("key-3")
    ht.delete("key-2")
    ht.delete("key-1")
    ht.delete("key-0")

    return_value = ht.get("key-0")
    print('print return vvaluuuuuuuuu',return_value)
    # ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")

