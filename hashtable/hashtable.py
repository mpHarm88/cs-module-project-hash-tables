class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):

        self.capacity = [MIN_CAPACITY if capacity < MIN_CAPACITY else capacity][0]
        self.ht = [None] * self.capacity
        self.item_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        load = self.item_count / self.capacity

        if load > .7:
            print("Load Factor >0.7, resizing larger")
            self.resize(self.capacity*2)
            self.get_load_factor()
        elif load < .2:
            print("Load Factor <0.2, resizing smaller")
            smaller_size = self.capacity//2
            self.resize([smaller_size if smaller_size >= 8 else 8 ][0])
            self.get_load_factor()
        
        return load


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        
         # hash := FNV_offset_basis do
        hashed_result = FNV_offset_basis
        key_bytes = key.encode()
        # for each byte_of_data to be hashed
        for byte in key_bytes:
        #     hash := hash × FNV_prime
            hashed_result = hashed_result * FNV_prime
        #     hash := hash XOR byte_of_data
            hashed_result = hashed_result ^ byte
        # return hash
        return hashed_result


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        x = 5381

        key_bytes = key.encode()

        for y in key_bytes:
            x = ((x << 5) + x) + y

        return x

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Hash the key
        hash = self.djb2(key)

        # Create index
        idx = hash % self.capacity

        # Store it
        val = HashTableEntry(key, value)

        # If index is none then insert value
        if self.ht[idx] ==  None:
            self.ht[idx] = val
            self.item_count += 1

        # If key at index is equal to key then change value
        elif self.ht[idx].key == key:
            self.ht[idx].value = value


        # if key is not present then insert at end of list
        elif self.ht[idx].next == None:
            self.ht[idx].next = val
            self.item_count += 1
        
        # else change the next val to the value
        else: 
            self.ht[idx].next.value = value
        
        self.get_load_factor()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # Find hash
        hash = self.djb2(key)

        # Get index
        idx = hash % self.capacity

        if self.ht[idx] == None:
            return "Key not found"

        elif self.ht[idx].key == key:
            self.ht[idx] = None
            self.item_count -= 1
        
        elif self.ht[idx].next == None:
            return
        
        elif self.ht[idx].next.key == key:
            self.ht[idx].next = None
            self.item_count -= 1
        
        self.get_load_factor()

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Find the hash for the key
        hash = self.djb2(key)

        # Get index
        idx = hash % self.capacity

        if self.ht[idx] == None:
            return None

        # look for key in linked list
        while self.ht[idx].key != key:
            
            # if key is not found return none
            if self.ht[idx].next == None:
                return None
            else:
                self.ht[idx] = self.ht[idx].next
        
        # if key equals inputted key then return value
        if self.ht[idx].key == key:
            return self.ht[idx].value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        # save old hash table
        old_ht = self.ht

        # overwrite old hash table
        self.ht = [None] * new_capacity

        # overwrite old cpacity
        self.capacity = new_capacity

        # resize
        for x in old_ht:
            if x == None:
                continue
            else:
                self.put(x.key, x.value)

                if x.next == None:
                    continue
                else:
                    self.put(x.next.key, x.next.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
