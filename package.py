class Package:

    # A class to define a package that will be delivered by a truck
    # Defines the ID, delivery address, special delivery notes,
    # and whether it has been delivered, at the hub, or is in transit
    def __init__(self, id_num, address_id, address, city, state, zip_code, deadline, weight, notes, delivery_status):
        self.id_num = id_num
        self.address_id = address_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.delivery_status = delivery_status
        self.left_hub_time = None
        self.delivery_time = None
