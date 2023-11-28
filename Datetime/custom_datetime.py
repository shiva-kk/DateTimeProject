from datetime import datetime as dt

class CustomDatetime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            current_time = dt.utcnow()
            self.date_time = dt(current_time.year, current_time.month, current_time.day, hour, minute, second)
        else:
            self.date_time = dt(year, month, day, hour, minute, second)

    @classmethod
    def validate_date(cls, year, month, day):
        try:
            cls(year, month, day)
            return True
        except ValueError:
            return False

    @classmethod
    def date_difference(cls, date1, date2):
        if not isinstance(date1, cls) or not isinstance(date2, cls):
            raise ValueError("Invalid input. Both arguments must be instances of CustomDatetime class.")
        difference = date1.date_time - date2.date_time
        return difference.days, difference.days // 7, difference.days // 30

    @classmethod
    def date_from_string(cls, date_str):
        parsed_date = dt.fromisoformat(date_str)
        return cls(parsed_date.year, parsed_date.month, parsed_date.day, parsed_date.hour, parsed_date.minute, parsed_date.second)

    @staticmethod
    def format_iso_static(date_time):
        return date_time.isoformat()

    def format_iso(self):
        return self.date_time.isoformat()

    def format_human_readable(self):
        return self.date_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def format_human_readable_static(date_time):
        return date_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def gregorian_to_julian(date_time):
        # Example conversion (simplified for illustration purposes)
        return date_time.year - 2000  # Replace with a proper conversion logic

    @staticmethod
    def julian_to_gregorian(julian_date):
        # Example conversion (simplified for illustration purposes)
        return dt(year=julian_date + 2000, month=1, day=1)

    @staticmethod
    def calculate_weekday(date_time):
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekdays[date_time.weekday()]

    def weekday_calculation(self):
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekdays[self.date_time.weekday()]
