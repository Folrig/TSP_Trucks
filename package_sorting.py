import math
from address_book import AddressBook
from priority_queue import PriorityQueue


class PackageSorting:
    # A static class to presort packages based upon specific constraints
    @staticmethod
    def sort_packages(unsorted_package_list):
        # Create variables to store our references
        sorted_package_list = []
        first_truck_load = []
        second_truck_load = []
        third_truck_load = []
        first_truck_addresses = []
        second_truck_addresses = []
        addresses = AddressBook.address_reference()
        # Find each item's destination ID to match the distance table
        for item in unsorted_package_list:
            for index in range(len(addresses)):
                if item.address == addresses[index][2]:
                    item.address_id = int(addresses[index][0])
        # Complexity of O(n)
        for package in unsorted_package_list:
            if 'Must' in package.notes or '09:00 AM' in package.deadline:
                first_truck_load.append(package)
                if package.address_id not in first_truck_addresses:
                    first_truck_addresses.append(package.address_id)
            elif 'Can only' in package.notes or 'Delayed' in package.notes or '10:30 AM' in package.deadline:
                if package.address_id not in second_truck_addresses:
                    second_truck_addresses.append(package.address_id)
                second_truck_load.append(package)
            elif 'Wrong' in package.notes:
                third_truck_load.append(package)
        for package in unsorted_package_list:
            if 'EOD' in package.deadline and 'N/A' in package.notes:
                if len(first_truck_load) < 16 and package.address_id in first_truck_addresses:
                    first_truck_load.append(package)
                elif len(second_truck_load) < 16 and package.address_id in second_truck_addresses:
                    second_truck_load.append(package)
                else:
                    third_truck_load.append(package)

        sorted_package_list.insert(0, first_truck_load)
        sorted_package_list.insert(1, second_truck_load)
        sorted_package_list.insert(2, third_truck_load)
        return sorted_package_list
