import math
from address_book import AddressBook
from priority_queue import PriorityQueue


class PackageSorting:
    # A static class to presort packages based upon specific constraints
    @staticmethod
    def sort_packages(unsorted_package_list):
        # Create variables to store our references
        priority_queue = PriorityQueue()
        sorted_package_list = []
        first_truck_load = []
        second_truck_load = []
        third_truck_load = []
        addresses = AddressBook.address_reference()
        distances = AddressBook.distance_reference()
        # Find each item's destination ID to match the distance table
        for item in unsorted_package_list:
            # TODO THIS IS PROBABLY INCORRECT. LOOK HERE IF ERRORS OCCUR
            for index in range(len(addresses)):
                if item.address == addresses[index][2]:
                    # TODO remove print statement for checking
                    # print(int(addresses[index][0]))
                    item.address_id = int(addresses[index][0])
        # Complexity of O(n)
        for package in unsorted_package_list:
            if 'Must' in package.notes or '09:00 AM' in package.deadline:
                first_truck_load.append(package)
            elif 'Can only' in package.notes or 'Delayed' in package.notes or '10:30 AM' in package.deadline:
                second_truck_load.append(package)
            elif 'Wrong' in package.notes:
                third_truck_load.append(package)
        for package in unsorted_package_list:
            if 'EOD' in package.deadline and 'N/A' in package.notes:
                if len(first_truck_load) < 16:
                    first_truck_load.append(package)
                elif len(second_truck_load) < 16:
                    second_truck_load.append(package)
                else:
                    third_truck_load.append(package)

        current_loc = 0
        # Perform sorting into priority while any unsorted packages remain
        while len(unsorted_package_list) > 0:
            smallest_distance = math.inf
            closest_package = None
            # Find the shortest distance between truck location and each loaded package
            for item in unsorted_package_list:
                distance_curr_loc_and_item = float(distances[current_loc][item.address_id])
                if distance_curr_loc_and_item <= smallest_distance:
                    smallest_distance = distance_curr_loc_and_item
                    closest_package = item
            # Once found, place package in priority queue using distance
            # Update current location to package's destination
            # Remove package from unorganized load
            if closest_package is not None:
                priority_queue.push(smallest_distance, closest_package)
                current_loc = closest_package.address_id
                unsorted_package_list.remove(closest_package)
            else:
                print('ERROR IN EFFICIENCY ALGORITHM')
        return priority_queue

        sorted_package_list.insert(0, first_truck_load)
        sorted_package_list.insert(1, second_truck_load)
        sorted_package_list.insert(2, third_truck_load)
        return sorted_package_list
