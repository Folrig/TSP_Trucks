class PackageSorting:
    # A static class to presort packages based upon specific constraints
    @staticmethod
    def sort_packages(*unsorted_package_list):
        sorted_package_list = []
        first_truck_load = []
        second_truck_load = []
        third_truck_load = []

        # TODO finish package sorting logic
        for package in unsorted_package_list:
            if 'Must' in package.notes:
                first_truck_load.append(package)
            if 'Can only' in package.notes:
                second_truck_load.append(package)
            if 'Delayed' in package.notes:
                second_truck_load.append(package)

        sorted_package_list.insert(0, first_truck_load)
        sorted_package_list.insert(1, second_truck_load)
        sorted_package_list.insert(2, third_truck_load)
        return sorted_package_list