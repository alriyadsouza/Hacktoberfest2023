class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
        raise KeyError(key)

# Example usage:
if __name__ == "__main__":
    hash_table = HashTable(10)

    hash_table.put("key1", "value1")
    hash_table.put("key2", "value2")

    print("Value for key1:", hash_table.get("key1"))
    print("Value for key2:", hash_table.get("key2"))

    hash_table.remove("key1")

    try:
        print("Value for key1:", hash_table.get("key1"))
    except KeyError:
        print("Key1 not found in the hash table.")
