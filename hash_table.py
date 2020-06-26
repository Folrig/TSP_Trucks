class HashTable:

    # A data structure class to be utilized for data organization using key-value pairs
    def __init__(self):
        capacity = 10
        self.bucket_list = []
        for i in range(capacity):
            self.bucket_list.append([])

    # An insertion function that stores all a package's info
    def insert(self, package):
        # Select the bucket to store the package
        bucket = hash(package) % len(self.bucket_list)