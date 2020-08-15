import math
from address_book import AddressBook
from priority_queue import PriorityQueue


class EfficiencyAlgorithm:
    @staticmethod
    def organize_route(unsorted_list):
        # Create variables to store our references
        priority_queue = PriorityQueue()
        addresses = AddressBook.address_reference()
        distances = AddressBook.distance_reference()
        current_loc = 0
        # Find each item's destination ID to match the distance table
        for item in unsorted_list:
            # TODO THIS IS PROBABLY INCORRECT. LOOK HERE IF ERRORS OCCUR
            for index in range(len(addresses)):
                if item.address == addresses[index][2]:
                    # TODO remove print statement for checking
                    # print(int(addresses[index][0]))
                    item.address_id = int(addresses[index][0])
        # Perform sorting into priority while any unsorted packages remain
        while len(unsorted_list) > 0:
            smallest_distance = math.inf
            closest_package = None
            # Find the shortest distance between truck location and each loaded package
            for item in unsorted_list:
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
                unsorted_list.remove(closest_package)
            else:
                print('ERROR IN EFFICIENCY ALGORITHM')
        return priority_queue
