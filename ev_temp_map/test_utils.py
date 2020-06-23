"""
Test cases for utils module
"""
import unittest

from .utils import get_temperature
from .utils import get_lat_lon_mask
from .utils import get_zone


# Global variables used in each test
TEST_FILE = "./ev_temp_map/test_data/20200101.nc4"


class TestUtils(unittest.TestCase):

    def test_get_temperature(self):
        """
        Test case for `get_temperature`
        """
        # test handling illegal input, file does not exist
        try:
            get_temperature("not_a_path")
            raise Exception("Illegal input test failed")
        except AssertionError:
            pass

        # test handling illegal input, filepath not a string
        try:
            get_temperature(3.1415926)
            raise Exception("Illegal input test failed")
        except AssertionError:
            pass

        temp = get_temperature(TEST_FILE)

        assert len(temp.shape) == 2, "Wrong variable dimension!"
        assert temp.any()

    def test_get_lat_lon_mask(self):
        """
        Test case for `get_lat_lon_mask`
        """
        # test handling illegal input, file does not exist
        try:
            get_lat_lon_mask("not_a_file.what")
            raise Exception("Illegal input test failed")
        except AssertionError:
            pass

        # test handling illegal input, filepath not a string
        try:
            get_lat_lon_mask(3.1415926)
            raise Exception("Illegal input test failed")
        except AssertionError:
            pass

        lat, lon, mask = get_lat_lon_mask(TEST_FILE)
        assert len(lat.shape) == 1, "Wrong variable dimension!"
        assert len(lon.shape) == 1, "Wrong variable dimension!"
        assert len(mask.shape) == 2, "Wrong variable dimension!"

    def test_get_zone(self):
        """
        Test case for `get_zone`
        """
        # test handling illegal input, wrong data type
        try:
            get_zone("not_a_number", "not_a_number")
            raise Exception("Illegal input test failed")
        except AssertionError:
            pass

        # test handling illegal input, out of range
        try:
            get_zone(100.00000001)
            raise Exception("Illegal input test failed")
        except AssertionError:
            pass

        assert get_zone(0) == "0.0 - 10.0",\
            "Something wrong with the algorithm! Got '" + get_zone(0) +\
            "' instead of '0.0 - 10.0'"
        assert get_zone(3.1415) == "0.0 - 10.0",\
            "Something wrong with the algorithm! Got '" + get_zone(3.1415) +\
            "' instead of '0.0 - 10.0'"
        assert get_zone(50) == "50.0 - 60.0",\
            "Something wrong with the algorithm! Got '" + get_zone(50) +\
            "' instead of '50.0 - 60.0'"
        assert get_zone(100) == "90.0 - 100.0",\
            "Something wrong with the algorithm! Got '" + get_zone(100) +\
            "' instead of '90.0 - 100.0'"
        assert get_zone(99.99, 12) == "96.0 - 100.0",\
            "Failed to limit range to 100! Got '" + get_zone(99.999999)\
            + "' instead of '96.0 - 100.0'"
