class Time:

    # A static class to take a time in HH:MM:SS and adjust it by minutes
    @staticmethod
    def adjust_time(time, time_passed):
        time_str = time
        time_str_arr = time_str.split(':')
        hours = int(time_str_arr[0])
        minutes = int(time_str_arr[1])
        seconds = int(time_str_arr[2])
        time_of_day = str.upper(time_str_arr[3])

        seconds_passed = int(60 * (time_passed % 1.0))
        seconds += seconds_passed

        minutes_passed = int(time_passed)
        minutes += minutes_passed

        if seconds >= 60:
            seconds -= 60
            minutes += 1

        if minutes >= 60:
            minutes -= 60
            hours += 1

        if hours >= 13:
            hours -= 12
            if time_of_day is 'AM':
                time_of_day = 'PM'
            elif time_of_day is 'PM':
                time_of_day = 'AM'

        return '{:02d}:{:02d}:{:02d} {}'.format(int(hours), int(minutes), int(seconds), time_of_day)