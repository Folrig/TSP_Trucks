class Time:

    # TODO make sure all time uses format of HH:MM:AM for data reading
    # TODO make sure all time uses format of HH:MM AM for input and return values

    @staticmethod
    # A static method to adjust the time string into human readable form
    def human_format(time):
        time_str = time
        time_str_arr = time_str.split(':')
        hours = time_str_arr[0]
        minutes = time_str_arr[1]
        time_of_day = str.upper(time_str_arr[3])
        return '{:02d}:{:02d} {}'.format(hours, minutes, time_of_day)

    # A static method to adjust the time string for data usage
    @staticmethod
    def data_format(time):
        time_str = time
        time_str_arr = time_str.split(':')
        hours = time_str_arr[0]
        minutes = time_str_arr[1]
        time_of_day = str.upper(time_str_arr[3])
        return '{:02d}:{:02d} {}'.format(hours, minutes, time_of_day)

    # A static method to take a time in HH:MM:SS and adjust it by minutes
    @staticmethod
    def adjust_time(time, time_passed):
        time_str = time
        time_str_arr = time_str.split(' ')
        time_str_arr = time_str_arr.split(':')
        hours = float(time_str_arr[0])
        minutes = float(time_str_arr[1])
        time_of_day = str.upper(time_str_arr[2])

        hours_passed = int(minutes) / 60
        minutes_passed = int(minutes - (hours_passed * 60))
        hours += hours_passed
        minutes += minutes_passed

        if minutes >= 60:
            minutes -= 60
            hours += 1

        if hours >= 13:
            hours -= 12
            if time_of_day is 'AM':
                time_of_day = 'PM'
            elif time_of_day is 'PM':
                time_of_day = 'AM'

        return '{:02d}:{:02d}:{:02d}:{}'.format(int(hours), int(minutes), int(seconds), time_of_day)