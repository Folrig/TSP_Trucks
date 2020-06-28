# A class to represent the trip of a delivery truck and track the time and distance traveled


class Truck:
    def __init__(self, current_time, current_load):
        self.current_time = current_time
        self.current_load = list(current_load)
        for package in current_load:
            package.delivery_status = 'En route'
            package.left_hub_time = current_time
        self.max_load = 16  # we probably won't need this
        self.total_distance = 0.0
        self.address_reference = []
        for row in open('address_data.csv'):
            self.address_reference.append(row.split(','))
        self.distance_reference = []
        for row in open('distance_data.csv'):
            self.distance_reference.append(row.split(','))
        self.current_location = 0
        self.next_location = 0

    def begin_delivery(self):
        while len(self.current_load) > 0:
            for package in self.current_load:
                # run algorithm to find shortest distance, should be easy
                # Should just be shortest_distance = algorithm.function(current_location, package.address)
                # Begin next for loop
                self.next_location = package.address_id
                trip_distance = self.distance_reference[self.current_location][self.next_location]
                trip_duration = trip_distance / 18.0
                # ************ self.current_time = Time(current_time, trip_duration)
                self.total_distance += trip_distance
                package.delivery_status = 'Delivered'
                package.delivery_time = self.current_time
                self.current_location = package.address_id
                self.current_load.remove(package)