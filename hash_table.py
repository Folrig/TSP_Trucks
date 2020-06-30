class HashTable:
    # A data structure class to be utilized for data organization
    # using key-value pairs
    def __init__(self):
        capacity = 40
        self.bucket_list = []
        for i in range(capacity):
            self.bucket_list.append([])

    # An insertion function places an item into the hash table
    def insert(self, package):
        # Select the bucket to store the package
        bucket = hash(package) % len(self.bucket_list)
        bucket_list = self.bucket_list[bucket]
        # Store package into the list of buckets
        bucket_list.append(package)

    # Look up function that uses a package's ID and returns the correspond
    # package's info
    def look_up(self, package_id_num):
        # Identify the bucket that the package is in by its ID
        bucket = hash(package_id_num) % len(self.bucket_list)
        # Return the package if it is found in the bucket list
        if package_id_num in self.bucket_list[bucket]:
            package_index = self.bucket_list.index(package_id_num)
            return self.bucket_list[package_index]
        # Return nothing if the package is not found
        else:
            return None