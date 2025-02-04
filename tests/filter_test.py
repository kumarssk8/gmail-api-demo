import unittest

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from rules.filter import StringFilter, DateFilter

class TestFilter(unittest.TestCase):
    
    def test_string_contains_filter(self):
        string_filter = StringFilter("from_address","contains","abc")
        condition = string_filter.derive_condition()
        self.assertEqual(condition, 'from_address like "%abc%"', "string contains check failed")
    
    def test_string_does_not_contain_filter(self):
        string_filter = StringFilter("from_address","does_not_contain","abc")
        condition = string_filter.derive_condition()
        self.assertEqual(condition, 'from_address not like "%abc%"', "string does not contain check failed")

    def test_string_equal_filter(self):
        string_filter = StringFilter("from_address", "equals", "abc")
        condition = string_filter.derive_condition()
        self.assertEqual(condition, 'from_address = "abc"', "string equal check failed")
    
    def test_string_does_not_equal_filter(self):
        string_filter = StringFilter("from_address", "does_not_equal", "abc")
        condition = string_filter.derive_condition()
        self.assertEqual(condition, 'from_address != "abc"', "string does not equal check failed")
    
    def test_date_less_than_filter_days(self):
        value = 2
        date_filter = DateFilter("date_received", "less_than", value, "day(s)")
        condition = date_filter.derive_condition()
        filter_date = date.today() + timedelta(days=-value)
        self.assertEqual(condition, f'date_received < "{filter_date}"', "date filter less than check failed")

    def test_date_greater_than_filter_days(self):
        value = 2
        date_filter = DateFilter("date_received", "greater_than", value, "day(s)")
        condition = date_filter.derive_condition()
        filter_date = date.today() + timedelta(days=-value)
        self.assertEqual(condition, f'date_received > "{filter_date}"', "date filter less than check failed")
    
    # def test_date_less_than_filter_months(self):
    #     value = 2
    #     date_filter = DateFilter("date_received", "less_than", value, "month(s)")
    #     condition = date_filter.derive_condition()
    #     filter_date = date.today() + relativedelta(month=-value)
    #     self.assertEqual(condition, f'date_received < "{filter_date}"', "date filter less than check failed")
    
    # def test_date_greater_than_filter_months(self):
    #     value = 2
    #     date_filter = DateFilter("date_received", "greater_than", value, "month(s)")
    #     condition = date_filter.derive_condition()
    #     filter_date = date.today() + relativedelta(month=-value)
    #     self.assertEqual(condition, f'date_received > "{filter_date}"', "date filter less than check failed")




if __name__ == "__main__":
    TestFilter().test_date_less_than_filter()