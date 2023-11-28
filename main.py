from Datetime.custom_datetime import CustomDatetime

def main():
    # Create an instance with the current date and time
    current_datetime = CustomDatetime()
    print("Current Datetime:", current_datetime.format_human_readable())

    # Create an instance with specific date and time
    specific_datetime = CustomDatetime(2023, 11, 11, 12, 30, 45)
    print("Specific Datetime (ISO):", specific_datetime.format_iso())
    print("Specific Datetime (Human-Readable):", specific_datetime.format_human_readable())

    # Validate a date
    is_valid = CustomDatetime.validate_date(2023, 11, 11)
    print("Is Valid Date:", is_valid)

    # Calculate date difference
    date1 = CustomDatetime(2023, 11, 11)
    date2 = CustomDatetime(2023, 11, 1)
    days_diff, weeks_diff, months_diff = CustomDatetime.date_difference(date1, date2)
    print("Days Difference:", days_diff)
    print("Weeks Difference:", weeks_diff)
    print("Months Difference:", months_diff)

    # Create a date from a string
    date_str = "2023-11-11T12:30:45"
    date_from_str = CustomDatetime.date_from_string(date_str)
    print("Date from String:", date_from_str.format_human_readable())

    # Calculate weekday
    weekday = CustomDatetime.calculate_weekday(current_datetime.date_time)
    print("Current Weekday:", weekday)

if __name__ == "__main__":
    main()
