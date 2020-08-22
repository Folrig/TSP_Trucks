# James Spencer  ID: 000486930


import math
from address_book import AddressBook
from priority_queue import PriorityQueue


class EfficiencyAlgorithm:
    # A static class that contains the algorithm for
    # taking an unsorted list and assigning the delivery
    # priority based upon delivery deadlines and similar
    # addresses. Returns a PriorityQueue data structure
    # Complexity of algorithm is O(n^2)
    @staticmethod
    def organize_route(unsorted_list):
        # Create variables to store our references
        nine_am_deadlines = []
        ten_am_deadlines = []
        eod_deadlines = []
        for item in unsorted_list:
            if '9:00 AM' in item.deadline:
                nine_am_deadlines.append(item)
        for item in unsorted_list:
            if '10:30 AM' in item.deadline:
                ten_am_deadlines.append(item)
        for item in unsorted_list:
            if 'EOD' in item.deadline:
                eod_deadlines.append(item)
        # Sort each deadline by distance
        nine_am_deadlines = EfficiencyAlgorithm.sort_by_distance(nine_am_deadlines)
        ten_am_deadlines = EfficiencyAlgorithm.sort_by_distance(ten_am_deadlines)
        eod_deadlines = EfficiencyAlgorithm.sort_by_distance(eod_deadlines)
        # Merge all lists into one PriorityQueue
        sorted_priority_queue = PriorityQueue()
        priority_value = 1
        for item in nine_am_deadlines:
            sorted_priority_queue.push(priority_value, item)
            priority_value += 1
        for item in ten_am_deadlines:
            sorted_priority_queue.push(priority_value, item)
            priority_value += 1
        for item in eod_deadlines:
            sorted_priority_queue.push(priority_value, item)
            priority_value += 1
        # Adjust priorities of packages based on if they have the same delivery address
        # Complexity of O(n^2) because of nested for-loops
        for i in range(0, len(sorted_priority_queue.queue)):
            j = i + 1
            for j in range(i, len(sorted_priority_queue.queue) - 1):
                if sorted_priority_queue.queue[j].item.address_id == sorted_priority_queue.queue[i].item.address_id:
                    sorted_priority_queue.queue[j].priority = sorted_priority_queue.queue[i].priority
        return sorted_priority_queue

    # Helper method that looks for distances between packages
    # Complexity is O(n^2) due to for loop nested
    # within the while loop
    @staticmethod
    def sort_by_distance(unsorted_list):
        distances = AddressBook.distance_reference()
        current_loc = 0
        closest_package = None
        sorted_list = []
        while len(unsorted_list) > 0:
            smallest_distance = math.inf
            for item in unsorted_list:
                distance = float(distances[current_loc][item.address_id])
                if distance <= smallest_distance:
                    smallest_distance = distance
                    closest_package = item
            # Once found, place package in priority queue using distance
            # Update current location to package's destination
            # Remove package from unorganized load
            if closest_package is not None:
                sorted_list.append(closest_package)
                current_loc = closest_package.address_id
                unsorted_list.remove(closest_package)
            else:
                print('ERROR IN SORT_BY_DISTANCE')
        return sorted_list
