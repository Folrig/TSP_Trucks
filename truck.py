from address_book import AddressBook
from time import Time
from priority_queue import PriorityQueue


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
                self.next_loc = package.item.address_id
                trip_distance = AddressBook.distance_reference()[self.current_loc][self.next_loc]
                trip_duration = trip_distance / 18.0
                self.current_time = Time.adjust_time(self.current_time, trip_duration)
                self.total_distance += trip_distance
                package.item.delivery_time = self.current_time
                if package.item.delivery_time <= package.item.deadline:
                    package.item.delivery_status = 'Delivered on time'
                elif package.item.delivery_time > package.item.deadline:
                    package.item.delivery_status = '*** DELIVERED LATE ***'
                else:
                    package.item.delivery_status = 'Package lost. Delivery unknown'
                self.current_loc = package.item.address_id
                self.current_load.pop()
                if self.current_load.is_empty():
                    self.next_loc = 0
        trip_distance = AddressBook.distance_reference()[self.current_loc][self.next_loc]
        trip_duration = trip_distance / 18.0
        self.current_time = Time.adjust_time(self.current_time, trip_duration)
        self.total_distance += trip_distance

    def get_distance(self):
        return self.total_distance