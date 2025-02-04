from abc import ABC, abstractmethod
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta

class Filter(ABC):
    def __init__(self, field, condition, value):
        self._field = field
        self._condition = condition
        self._value = value

    @abstractmethod
    def derive_condition(self):
        pass

class StringFilter(Filter):
    
    def derive_condition(self):
        condition_map = {
            "contains": f'{self._field} like "%{self._value}%"',
            "does_not_contain": f'{self._field} not like "%{self._value}%"',
            "equals": f'{self._field} = "{self._value}"',
            "does_not_equal": f'{self._field} != "{self._value}"'
        }
        if self._condition not in condition_map:
            raise RuntimeError(f'String condition {self._condition} not present')
        return condition_map[self._condition]

class DateFilter(Filter):
    def __init__(self, field, condition, value, units):
        super().__init__(field, condition, value)
        self._units = units

    _date_conditions = ["less_than", "greater_than"]
    _units_condition = ["day(s)", "month(s)"]

    def derive_condition(self):
        if self._condition not in self._date_conditions:
            raise RuntimeError(f"Invalid date condition {self._condition}")
        
        if type(self._value) != int:
            raise RuntimeError(f"Integer type of value is expected for dete filter")
        
        if self._units not in self._units_condition:
            raise RuntimeError(f"Invalid units {self._units}. Allowed units {self._units_condition}")
        
        filter_date = date.today() + (relativedelta(month=-self._value) if self._units_condition == "month(s)" else timedelta(days=-self._value)) 
        
        print(f"filtered data {filter_date}")

        if self._condition == "less_than":
            return f"{self._field} < {filter_date}"
        else:
            return f"{self._field} > {filter_date}"
         
