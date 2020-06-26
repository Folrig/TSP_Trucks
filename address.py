class Address:

    # A class to hold the data for a delivery address
    def __init__(self, id_num, name, street, city, state, zip_code):
        self.id_num = id_num
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code