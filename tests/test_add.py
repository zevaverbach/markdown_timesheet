from datetime import time

from pytest import fixture

from app.add import (
    split_time_range_string,
    add_up_timesheet,
    find_time_ranges,
    parse_time,
    subtract_times,
)
from app.config import SAMPLE_TIMESHEET_PATH


@fixture
def timesheet() -> str:
    with open(SAMPLE_TIMESHEET_PATH) as fin:
        return fin.read()


@fixture
def string_with_no_times():
    return "## no times here 123"


@fixture
def time_range_strings():
    return ["9:30-12:30", "8:30-7:30"]


@fixture
def time_ranges():
    return [["9:30", "12:30"], ["8:30", "7:30"]]


@fixture
def times():
    return [(time(9, 30), time(12, 30)), (time(8, 30), time(7, 30))]


@fixture
def string_with_times():
    return "## 9:30-12:30, 8:30-7:30 "


def test_add_up_timesheet(timesheet):
    assert add_up_timesheet(timesheet) == 430


def test_find_time_ranges_none(string_with_no_times):
    assert find_time_ranges(string_with_no_times) == []


def test_find_time_ranges(string_with_times, time_range_strings):
    assert find_time_ranges(string_with_times) == time_range_strings


def test_split_time_range_string(time_range_strings, time_ranges):
    for time_range_string, time_range_tuple in zip(time_range_strings, time_ranges):
        assert split_time_range_string(time_range_string) == time_range_tuple


def test_parse_time(time_ranges, times):
    for time_range_tuple, time_tuple in zip(time_ranges, times):
        for time_string, time_ in zip(time_range_tuple, time_tuple):
            assert parse_time(time_string) == time_


def test_subtract_times(times):
    assert subtract_times(*times[0]) == 180
    assert subtract_times(*times[1]) == 1380
