import csv

from efficiency_algorithm import EfficiencyAlgorithm
from hash_table import HashTable
from package_sorting import PackageSorting
from truck import Truck
from my_time import Time
from package import Package
from priority_queue import PriorityQueue


def main():
    # Create hash table for packages
    package_hash_table = HashTable()
    # Create 40 packages and assign the address IDs
    all_packages = []
    with open('package_data.csv') as data:
        package_data = csv.reader(data, delimiter=',')
        for row in package_data:
            package = Package(row[0], None, row[1], row[2], row[3], row[4], row[5], row[6], row[7], 'At hub')
            all_packages.append(package)
    # Add packages to hash table
    for package in all_packages:
        package_hash_table.insert(package.id_num, package)
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
    first_truck.begin_delivery('08:00 AM')
    second_truck.begin_delivery('09:05 AM')
    # Take address change for package #9 into account
    if first_truck.current_time >= '10:20 AM':
        for queue_item in third_load.queue:
            if 'Wrong address' in queue_item.item.notes:
                queue_item.item.address_id = 19
                queue_item.item.address = '410 S State St'
                queue_item.item.zip_code = '84111'
    # Because there are only two drivers, wait until the first returns
    # before sending out the third one
    if first_truck.current_loc == 0:
        if first_truck.current_time <= '10:20:AM':
            # Take address change into account if not already done
            for queue_item in third_load.queue:
                if 'Wrong address' in queue_item.item.notes:
                    queue_item.item.address_id = 19
                    queue_item.item.address = '410 S State St'
                    queue_item.item.zip_code = '84111'
            third_truck.begin_delivery('10:20 AM')
        else:
            third_truck.begin_delivery(first_truck.current_time)
    # Create menu for input here to check things
    user_interface(package_hash_table, first_truck, second_truck, third_truck)


def user_interface(hash_table, first_truck, second_truck, third_truck):
    selection = 0
    while selection != 3:
        print('\n\nWelcome to the WGUPS Delivery System')
        print('Today\'s route was completed by', third_truck.current_time)
        total_distance = float(first_truck.get_distance()) + \
            float(second_truck.get_distance()) + float(third_truck.get_distance())
        print('Total distance traveled was:', "{0:.2f}".format(total_distance, 2), 'miles')
        print('Please make a selection:')
        print('1: Search for package information by package ID')
        print('2: Print delivery status of packages at a specific time')
        print('3: Exit program')
        selection = int(input())
        if selection == 1:
            package_id_input = input('Enter a package ID to search for: ')
            package = hash_table.get(package_id_input)
            package.__str__()
        elif selection == 2:
            time_input = input('Enter a time to search for deliveries in HH:MM AM/PM'
                               ', example: 9:30 AM: ')
            try:
                time_input = Time.to_data_format(time_input, True)
                for bucket in hash_table.bucket_list:
                    for value in bucket:
                        print_package_info_at_time(time_input, value[1])
            except ValueError:
                print('Invalid time entry')
        elif selection == 3:
            print('Thank you for using the system.')
        else:
            print('Please enter a valid menu option')
            print('\n\n')


def print_package_info_at_time(time_input, package):
    if time_input < package.left_hub_time:
        left_hub_time = 'At hub'
        delivery_time = 'N/A'
        delivery_status = 'At hub'
    elif time_input <= package.delivery_time:
        left_hub_time = package.left_hub_time
        delivery_time = 'N/A'
        delivery_status = 'En route'
    elif time_input >= package.delivery_time:
        left_hub_time = package.left_hub_time
        delivery_time = package.delivery_time
        delivery_status = package.delivery_status
    else:
        print('Error in print package info at time')
        left_hub_time = None
        delivery_time = None
        delivery_status = None
    print('\nPackage:', package.id_num, '\nDestination:', package.address, package.city, package.state, package.zip_code,
          '\nWeight:', package.weight, 'kg', '\nDeadline:', package.deadline,
          '\nLeft hub at:', left_hub_time, '\tDelivery Time:', delivery_time,
          '\tDelivery Status:', delivery_status, '\n')


if __name__ == '__main__':
    main()
