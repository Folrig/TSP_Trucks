from address_book import AddressBook
from my_time import Time


class Truck:
    # A class to represent the trip of a delivery truck and track the time and
    # distance traveled
    def __init__(self, current_load):
        self.current_time = ''
        self.current_load = current_load  # This is a PriorityQueue
        self.total_distance = 0.0
        self.current_loc = 0
        self.next_loc = 0

    def begin_delivery(self, depart_time):
        self.current_time = depart_time
        # Begin delivery, set package attributes
        for package in self.current_load.queue:
            package.item.delivery_status = 'En route'
            package.item.left_hub_time = self.current_time
        # Deliver packages until there are none loaded
        while self.current_load.get_length() > 0:
            # Deliver a package
            for package in self.current_load.queue:
                # Set next location to where truck is headed
                self.next_loc = package.item.address_id
                # Find out how long the trip is going to take based on distance
                trip_distance = float(AddressBook.distance_reference()[self.current_loc][self.next_loc])
                trip_duration = float((trip_distance / 18.0) * 60.0)
                # Adjust the truck time and distance traveled
                self.current_time = Time.adjust_time(self.current_time, trip_duration)
                self.total_distance += trip_distance
                # Set the delivery time to when the truck arrives at destination
                package.item.delivery_time = self.current_time
                # Mark delivery status based upon
                # Time delivered vs. deadline. Mostly for algorithm checking
                if package.item.delivery_time <= package.item.deadline:
                    package.item.delivery_status = 'Delivered on time'
                elif package.item.delivery_time > package.item.deadline:
                    package.item.delivery_status = '*** DELIVERED LATE ***'
                else:
                    package.item.delivery_status = 'Package lost. Delivery unknown'
                # Change truck's current location to where package was delivered
                self.current_loc = package.item.address_id
                self.current_load.pop()
                # Check if the truck is empty, if it is then head back to the hub
                if self.current_load.is_empty():
                    self.next_loc = 0
        # Perform time and distance adjustments for heading back to the hub
        # trip_distance = AddressBook.distance_reference()[self.current_loc][self.next_loc]
        # trip_duration = float((trip_distance / 18.0) * 60.0)
        # self.current_time = Time.adjust_time(self.current_time, trip_duration)
        # self.total_distance += trip_distance

    def get_distance(self):
        return self.total_distance