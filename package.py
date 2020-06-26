class Package:

    # A class to define a package that will be delivered by a truck
    def __init__(self, id_num, address, deadline, city, zip_code, weight, status):
        self.id_num = id_num
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status