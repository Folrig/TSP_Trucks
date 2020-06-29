class AddressBook:
    # A static class to use as a reference for all other classes to look up
    # addresses and distances
    @staticmethod
    def address_reference():
        address_reference = []
        for row in open('address_data.csv'):
            address_reference.append(row.split(','))
        return address_reference

    @staticmethod
    def distance_reference():
        distance_reference = []
        for row in open('distance_data.csv'):
            distance_reference.append(row.split(','))
        return distance_reference