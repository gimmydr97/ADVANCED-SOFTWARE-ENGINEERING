
from datetime import datetime
from myservice.classes.reservation import Reservation
import sys

_TEST_CLOCK = datetime.now()

def is_in_future(datetime):
    return datetime > get_current_datetime()

def get_current_datetime():
    global _TEST_CLOCK

    if "pytest" in sys.modules:
        return _TEST_CLOCK
    else:
        return datetime.now().strftime("%d/%m/%Y %H:%M")

def main():
    print(datetime.now().strftime("%d/%m/%Y %H:%M"))
    print(type(datetime.strptime("01/04/2020 20:30", '%d/%m/%Y %H:%M')))
    print(is_in_future("20/12/2021 20:30"))
if __name__ == '__main__':
    main()