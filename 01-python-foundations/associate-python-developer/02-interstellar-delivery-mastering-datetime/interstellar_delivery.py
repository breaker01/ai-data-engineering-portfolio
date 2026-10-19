# Start coding here. Use as many cells as you need.
from datetime import datetime, timedelta

def format_date(timestamp, datetime_format):
    return datetime.fromtimestamp(timestamp).strftime(datetime_format)


def calculate_landing_time(rocket_launch_dt, travel_duration):
    landing_dt = rocket_launch_dt + timedelta(days=travel_duration)
    return landing_dt.strftime("%d-%m-%Y")


def days_until_delivery(expected_delivery_dt, current_dt):
    return (expected_delivery_dt - current_dt).days
