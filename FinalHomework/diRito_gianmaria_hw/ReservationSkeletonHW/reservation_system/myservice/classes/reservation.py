from datetime import datetime


class Reservation():
    def __init__(self, id, name, date, hashed_psw, guests=[]):
        self.id = id
        self.name = name
        try:
            self.date = datetime.strptime(date, '%d/%m/%Y %H:%M')
        except:
            raise WrongDatetimeFormatError(
                "Wrong datetime format. Format is '%d/%m/%Y %H:%M', you sent '{}'".format(date))
        self.hashed_psw = hashed_psw
        self.guests = guests

    def serialize(self):
        return {'date': self.date.strftime("%d/%m/%Y %H:%M"),
                'guests': self.guests,
                'id': self.id,
                'name': self.name}

    def replace_guests(self, new_guests):
        self.guests = new_guests


class NonExistingReservationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class WrongPasswordError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class WrongDatetimeFormatError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

