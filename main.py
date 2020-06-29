# Currently used for testing works in process
# Will be used for logic of final program
from truck import Truck
from package import Package


def main():
    # Create hash table for packages
    # Create 40 packages and assign the address IDs
    # Add packages to hash table
    # Create 3 load lists based on package priorities, possibly in a different class
    # Run these lists through the sorting algorithm to computer the most efficient delivery order
    # Create 3 trucks with appropriate leaving times
    # Load the truck's current_load with the load list created
    # Have the trucks leave and do deliveries
    # Create menu for input here to check things
    first_load = []
    second_load = []
    third_load = []
    first_truck = Truck('08:00:00', first_load)
    second_truck = Truck('09:05:00', second_load)
    with first_truck.current_load is 0 and first_truck.current_loc is 0:
        third_truck = Truck(first_truck.current_time, third_load)

    # Create what we want to test and run here
    for row in first_truck.distance_reference:
        for column in row:
            print(column)


if __name__ == '__main__':
    main()