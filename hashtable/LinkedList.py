def find(self, value):
    cur = self.head
    while cur is not None:
        if cur.value == value:
             return cur
        cur = cur.next

        return none
#different for hash tables
#will be given a key
#need to see if key is =

def delete(self, value):
    #no previous value, assign to head
    cur = self.head

    if cur.value == value:
        #move head to next value
        self.head = cur.next
        #return node deleted
        return cur
    # past head
    prev = cur
    cur = cur.next

    while cur != None:
        if cur.value == value:
            #assign the previous nodes next, to current's next
            prev.next = cur.next
            return cur
        else:
            prev = cur 
            cur = cur.next
             

def insert(self, node):
    #reassign current head
    node.next = self.head
    self.head = node 