class HashTable:
    """
    A simple implementation of a hash table using lists.
    
    Attributes:
        size (int): The number of slots in the hash table.
        table (list): The underlying list storing key-value pairs.
    """
    
    def __init__(self, size=10):
        """
        Initialize the hash table with a fixed size.
        
        Args:
            size (int): Number of slots in the table. Default is 10.
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # Each slot holds a list (to handle collisions)
    
    def _hash(self, key):
        """
        Create a hash index for a given key.
        
        Args:
            key (str): The key to hash.
        
        Returns:
            int: The index within the table.
        """
        return sum(ord(char) for char in key) % self.size
    
    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        
        Args:
            key (str): The key to insert.
            value (any): The value associated with the key.
        """
        index = self._hash(key)
        # Check if key already exists → update value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, append new key-value pair
        self.table[index].append([key, value])
    
    def get(self, key):
        """
        Retrieve the value associated with a key.
        
        Args:
            key (str): The key to look up.
        
        Returns:
            any: The value if found, else None.
        """
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key):
        """
        Remove a key-value pair from the hash table.
        
        Args:
            key (str): The key to delete.
        """
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

# Create a hash table
ht = HashTable(size=5)

# Insert key-value pairs
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("grape", 30)

# Retrieve values
print(ht.get("apple"))   # Expected: 10
print(ht.get("banana"))  # Expected: 20
print(ht.get("grape"))   # Expected: 30
print(ht.get("pear"))    # Expected: None (not inserted)

# Update a value
ht.insert("apple", 99)
print(ht.get("apple"))   # Expected: 99

# Delete a key
ht.delete("banana")
print(ht.get("banana"))  # Expected: None
