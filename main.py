from efficiency_algorithm import EfficiencyAlgorithm
from hash_table import HashTable
from package_sorting import PackageSorting
from truck import Truck


def main():
    # Create hash table for packages
    package_hash_table = HashTable()
    # Create 40 packages and assign the address IDs
    all_packages = []
    for row in open('package_data.csv'):
        all_packages.append(row.split(','))
    # Add packages to hash table
    for package in all_packages:
        package_hash_table.insert(package)
    # Presort packages for each truck
    all_packages = PackageSorting.sort_packages(all_packages)
    # Create 3 load lists based on package priorities, possibly in a different class
    first_load = all_packages[0]
    second_load = all_packages[1]
    third_load = all_packages[2]
    # Run these lists through the sorting algorithm to computer the most efficient delivery order
    first_load = EfficiencyAlgorithm.organize_route(first_load)
    second_load = EfficiencyAlgorithm.organize_route(second_load)
    third_load = EfficiencyAlgorithm.organize_route(third_load)
    # Create and load 3 trucks
    first_truck = Truck(first_load)
    second_truck = Truck(second_load)
    third_truck = Truck(third_load)
    # Send the two drivers to begin deliveries at set times
    first_truck.begin_delivery('08:00:AM')
    second_truck.begin_delivery('09:05:AM')
    # Take address change for package #9 into account
    with first_truck.current_time is '10:20:AM':
        for package in third_load:
            if 'Wrong address' in package.notes:
                package.address_id = 19
                package.address = '410 S State St'
                package.zip_code = '84111'
    # Because there are only two drivers, wait until the first returns
    # before sending out the third one
    with first_truck.current_load is 0 and first_truck.current_loc is 0:
        if first_truck.current_time <= '10:20:AM':
            third_truck.begin_delivery('10:20:AM')
        else:
            third_truck.begin_delivery(first_truck.current_time)
    # Create menu for input here to check things
    # TODO Implement menu system here
    # TODO Create menu using a separate function with while loop


if __name__ == '__main__':
    main()