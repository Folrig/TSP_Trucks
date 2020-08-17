from address_book import AddressBook
from my_time import Time
from package import Package


class Truck:
    # A class to represent the trip of a delivery truck and track the time and
    # distance traveled
    number_of_trucks = 0

    def __init__(self, current_load):
        Truck.number_of_trucks += 1
        self.truck_id = Truck.number_of_trucks
        self.current_time = ''
        self.current_load = current_load  # This is a PriorityQueue
        self.total_distance = 0.0
        self.current_loc = 0
        self.next_loc = 0

    def begin_delivery(self, depart_time):
        self.current_time = depart_time
        # Begin delivery, set package attributes
        for package_queue_item in self.current_load.queue:
            package_queue_item.item.delivery_status = 'En route'
            package_queue_item.item.left_hub_time = self.current_time
        # Deliver packages until there are none loaded
        while self.current_load.get_length() > 0:
            # Find which address to deliver to first based upon next package in load
            # Index 0 will always have the highest priority because of removal
            current_priority_level = self.current_load.queue[0].priority
            self.next_loc = self.current_load.queue[0].item.address_id
            # Drive to that location and determine distance driven
            # Add to total distance
            # Use distance driven to determine time passed
            # Add time passed to current drive time
            trip_distance = float(AddressBook.distance_reference()[self.current_loc][self.next_loc])
            self.total_distance += trip_distance
            trip_duration = float((trip_distance / 18.0) * 60.0)
            self.current_time = Time.adjust_time(self.current_time, trip_duration)
            # Adjust current truck location to package location
            self.current_loc = self.current_load.queue[0].item.address_id
            # Update delivery status for all packages with the address/priority
            # Remove packages from load
            for package_item in list(self.current_load.queue):
                if package_item.priority == current_priority_level:
                    package_item.item.delivery_time = self.current_time
                    if package_item.item.delivery_time <= package_item.item.deadline:
                        package_item.item.delivery_status = 'Delivered on time'
                    elif package_item.item.delivery_time > package_item.item.deadline:
                        package_item.item.delivery_status = '*** DELIVERED LATE ***'
                    else:
                        package_item.item.delivery_status = 'Package lost. Delivery unknown'
                    self.current_load.queue.remove(package_item)
        # Return back to base if you are truck one and add that distance, adjust time
        if self.current_load.is_empty() and self.truck_id == 1:
            self.next_loc = 0
            trip_distance = float(AddressBook.distance_reference()[self.current_loc][self.next_loc])
            self.total_distance += trip_distance
            trip_duration = float((trip_distance / 18.0) * 60.0)
            self.current_time = Time.adjust_time(self.current_time, trip_duration)
            self.current_loc = 0

    def get_distance(self):
        return self.total_distance
