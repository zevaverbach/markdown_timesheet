from datetime import datetime, date, time
from dateutil import parser
from typing import List, Union, Tuple

from app.types_ import Minutes


def subtract_times(first: time, second: time) -> Minutes:
    return int(
        (
            datetime.combine(datetime(1, 1, 1, 0, 0, 0), second)
            - datetime.combine(date.today(), first)
        ).seconds
        / 60
    )


def add_up_timesheet(timesheet_string: str) -> Minutes:
    total_minutes = 0

    for line in timesheet_string.split("\n"):
        total_minutes += get_minutes(line)
    return total_minutes


def get_minutes(time_sheet_string_line):
    time_range_strings = find_time_ranges(time_sheet_string_line)

    if not time_range_strings:
        return 0

    for time_range_string in time_range_strings:
        start_string, end_string = split_time_range_string(time_range_string)
        start, end = map(parse_time, [start_string, end_string])
        return subtract_times(start, end)


def find_time_ranges(timesheet_line: str) -> Union[list, List[str]]:
    remove_hashes_and_leading_trailing_spaces = timesheet_line.replace("#", "").strip()
    try:
        parse_time(remove_hashes_and_leading_trailing_spaces)
    except ValueError:
        return []
    else:
        if ":" not in remove_hashes_and_leading_trailing_spaces:
            return []
        return remove_hashes_and_leading_trailing_spaces.split(", ")


def parse_time(time_string: str) -> time:
    return parser.parse(time_string).time()


def split_time_range_string(time_range_string) -> Tuple[str]:
    return time_range_string.split("-")
