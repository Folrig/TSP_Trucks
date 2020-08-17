class HashEntry:

    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashTable:
    # A data structure class to be utilized for data organization
    # using key-value pairs
    def __init__(self):
        capacity = 40
        self.bucket_list = []
        for i in range(capacity):
            self.bucket_list.append([])

    # Private getter to create a hash key
    # Complexity is O(1)
    def _get_hash(self, key):
        bucket = int(key) % len(self.bucket_list)
        return bucket

    # Insert a new package value into the hash table
    # Space-time complexity is O(N)
    def insert(self, key, item):
        key_hash = self._get_hash(key)
        key_value = [key, item]

        if self.bucket_list[key_hash] is None:
            self.bucket_list[key_hash] = list([key_value])
            return True
        else:
            for value in self.bucket_list[key_hash]:
                if value[0] == key:
                    value[1] = key_value
                    return True
            self.bucket_list[key_hash].append(key_value)
            return True

    # Look up function that uses a package's ID and returns the correspond
    # package's info
    # Complexity is O(N)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.bucket_list[key_hash] is not None:
            for value in self.bucket_list[key_hash]:
                if value[0] == key:
                    return value[1]
        return None
