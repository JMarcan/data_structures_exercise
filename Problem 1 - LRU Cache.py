class ItemObj:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        """ return value as a string when class is used in print statement self.items"""
        if self.value is None:
            return 'None'
        return str(self.value)


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity < 1:
            print ("Warrning: Input cache capacity was less than 1 ({0}). \
                   Cache is initialized with the capacity 1".format(capacity))
            capacity = 1
            
        print ("Cache initialized with the capacity: {0}".format(capacity))
        
        self.items = {}
        self.capacity = capacity
        self.num_entries = 0
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        
        item = self.items.get(key)
        
        print("\nGet Element with Key: {0}\n \
        Head: {1}\n \
        Tail: {2}\n \
        Items: {3}".format(key, self.head, self.tail, self.items))
        
        if item is None:
            return -1
        
        if item.prev is not None:
            self.items[item.prev].next = item.next
        else:
            print("Updating tail with key: {0}".format(key))
            self.tail = item.next
            
        if item.next is not None:
            self.items[item.next].prev = item.prev

        head = self.items.get(self.head, None)
        if head is not None:
            head.next = key

        item.prev = self.head
        item.next = None

        self.head = key
        
        return item.value
          

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        
        if self.capacity < 1:
            print("Cannot perform operations on cache capacity less than 1 (0}".format(self.capacity))
            return
        
        head = self.items.get(self.head)
        new_item = ItemObj(value)
        
        if head is None:
            self.head = key
            self.tail = key
        else:
            new_item.prev = self.head
            head.next = key
        
        self.items[key] = new_item
        self.head = key
        
        if len(self.items) > self.capacity:
            print("Cache capacity exceeded, deleting the last accessed item {0}".format(self.tail))
            tail = self.items[self.tail]
            del self.items[self.tail]
            self.tail = tail.next
    
    def size(self):
        return self.num_entries

def test_cases(cache_size):
    our_cache = LRU_Cache(cache_size)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    
    # TC 1
    if our_cache.get(1) == 1: # returns 1
        print ("1. Passed")
    else: 
        print ("1. Failed")
        
    # TC 2    
    if our_cache.get(2)  == 2: # returns 2
        print ("2. Passed")
    else: 
        print ("2. Failed")
        
    # TC 3    
    if our_cache.get(9)  == -1: # returns -1 because 9 is not presented in the cache
        print ("3. Passed")
    else: 
        print ("3. Failed")
        
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
    
    # TC 4
    if our_cache.get(3)  == -1: # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
        print ("4. Passed")
    else: 
        print ("4. Failed")
        
    # TC 5    
    if our_cache.get(-1)  == -1: # returns -1 because -1 index do not exists
        print ("5. Passed")
    else: 
        print ("5. Failed")
        
if __name__ == '__main__':
    # execute test cases  
    test_cases(5)    
    