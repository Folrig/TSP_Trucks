# James Spencer  ID: 000486930


class Time:
    # A static method to adjust the time string into human readable form
    @staticmethod
    def to_human_format(time):
        time_list = time.split(' ')
        time_str = str(time_list[0])
        time_of_day = str.upper(time_list[1])
        time_list = time_str.split(':')
        hours = int(time_list[0])
        minutes = str(time_list[1])
        formatted_time = str(hours) + ':' + minutes + ' ' + time_of_day
        return formatted_time

    # A static method to adjust the time string for data usage
    @staticmethod
    def to_data_format(time, is_data_format):
        time_list = time.split(' ')
        time_str = str(time_list[0])
        time_of_day = str.upper(time_list[1])
        time_list = time_str.split(':')
        hours = int(time_list[0])
        minutes = str(time_list[1])
        if is_data_format:
            if 'PM' in time_of_day:
                hours += 12
            if hours < 10:
                hours = str(hours)
                hours = '0' + hours
            formatted_time = str(hours) + ':' + minutes + ' ' + time_of_day
        else:
            formatted_time = str(hours) + ':' + minutes + ' ' + time_of_day
        return formatted_time

    # A static method to take a time in HH:MM:SS, adjust it by minutes
    # and return the new time after the minutes have passed
    @staticmethod
    def adjust_time(time, time_passed):
        time_list = time.split(' ')
        time_str = str(time_list[0])
        time_of_day = str.upper(time_list[1])
        time_list = time_str.split(':')
        hours = float(time_list[0])
        input_hours = float(time_list[0])
        minutes = float(time_list[1])

        hours_passed = int(time_passed / 60)
        minutes_passed = int(time_passed - (hours_passed * 60))
        hours += hours_passed
        minutes += minutes_passed

        if minutes >= 60:
            minutes -= 60
            hours += 1

        if hours >= 12 and input_hours <= 11:
            if time_of_day == 'AM':
                time_of_day = 'PM'
            elif time_of_day == 'PM':
                time_of_day = 'AM'

        if hours >= 13:
            hours -= 12

        formatted_time = '{:02d}:{:02d} {}'.format(int(hours), int(minutes), time_of_day)
        return formatted_time
