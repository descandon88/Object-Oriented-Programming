
# Add a class method from_str() that:
# accepts a string datestr of the format'YYYY-MM-DD',
# splits datestr and converts each part into an integer,
# returns an instance of the class with the attributes set to the values extracted from datestr.
class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        return cls(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)


# For compatibility, you also want to be able to convert a datetime object into a BetterDate object.

# Add a class method from_datetime() that accepts a datetime object as the argument, and uses its attributes .year, .month and .day to create a BetterDate object with the same attribute values.

from datetime import datetime
help(datetime)

class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
    
    @classmethod
    def from_datetime(cls, datetime):
      year, month, day =  datetime.year, datetime.month,datetime.day
      return cls(year, month, day)

# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)

