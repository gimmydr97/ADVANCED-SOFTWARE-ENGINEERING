import hashlib  # TODO: see docs at https://docs.python.org/3/library/hashlib.html
import json
import sys

from flakon import JsonBlueprint
from flask import request, jsonify, abort
from myservice.classes.reservation import Reservation, NonExistingReservationError, WrongPasswordError, WrongDatetimeFormatError
from datetime import datetime

reservations = JsonBlueprint('reservations', __name__)

_RESERVATIONS = {}  # list of reservations
_RESERVATION_ID = 0  # index of the last created reservation

# For testing purpose only. Ignore this variable.
_TEST_CLOCK = datetime.now()


@reservations.route("/reservations", methods=['GET', 'POST'])
def all_reservations():
    global _RESERVATION_ID

    if 'POST' == request.method:
        result = create_reservation(request)
        _RESERVATION_ID +=  1

    elif 'GET' == request.method:
        result = get_all_reservations()

    return result


@reservations.route("/reservations/count", methods=['GET'])
def count_reservations():

    jsonres = get_all_reservations().get_json()
    fr = len(jsonres['futurereservations'])

    return jsonify({'nreservations':fr})


@reservations.route("/reservation/<id>", methods=['GET', 'DELETE'])
def single_reservation(id):

    global _RESERVATIONS
    result = ""

    # TODO: check if the reservation exists
    exists_reservation(id)
    reservation =_RESERVATIONS[str(id)]

    if 'GET' == request.method:
        # TODO: retrieve the reservation with <id>
        result = jsonify({'reservation':reservation.serialize()})
    elif 'DELETE' == request.method:
        # TODO: delete a reservation, if not in the past, and return its id

        json_data = request.get_json()
        try:
            check_password(json_data['password'],reservation.hashed_psw)

            if "pytest" in sys.modules:
                date = datetime.strptime(reservation.serialize()['date'], '%d/%m/%Y %H:%M')
            else:
                date = reservation.serialize()['date']

            if is_in_future(date):
                _RESERVATIONS.pop(str(id),None)
                result = jsonify({'reservationid': str(id) })
            else:
                result = jsonify({'error': 'past reservation'})
                
        except WrongPasswordError :
            result = jsonify({'error': 'wrong password'})
    
    return result



@reservations.route("/reservation/<id>/guests", methods=['GET', 'PUT'])
def reservation_guests(id):
    global _RESERVATIONS
    result = ""

    # TODO: check if the reservation exists
    exists_reservation(id)
    reservation =_RESERVATIONS[str(id)]

    if 'GET' == request.method:
        # TODO: retrieve the number of guests for the reservation identified by <id>
        result = jsonify({'nguests':len(reservation.serialize()['guests'])})
    if 'PUT' == request.method:
        # TODO: edit the number of guests for the reservation identified by <id>
        json_data = request.get_json()
        try:
            check_password(json_data['password'],reservation.hashed_psw)
            
            if "pytest" in sys.modules:
                date = datetime.strptime(reservation.serialize()['date'], '%d/%m/%Y %H:%M')
            else:
                date = reservation.serialize()['date']

            if is_in_future(date):

                reservation.replace_guests(json_data['guests'])
                result = jsonify({'guests': tuple(reservation.serialize()['guests']) })

            else:
                result = jsonify({'error': 'past reservation'})

        except WrongPasswordError :
            result = jsonify({'error': 'wrong password'})
    
        # TODO: check password

        # TODO: check if is future reservation

    return result

############################################
# HELPER FUNCTIONS BELOW (use them, do not change them!)
############################################


def exists_reservation(id):
    if int(id) > _RESERVATION_ID:
        abort(404)  # error 404: Not Found, i.e. wrong URL, resource does not exist
    elif not(id in _RESERVATIONS):
        abort(410)  # error 410: Gone, i.e. it existed but it's not there anymore


def get_current_datetime():
    global _TEST_CLOCK

    if "pytest" in sys.modules:
        return _TEST_CLOCK
    else:
        return datetime.now().strftime("%d/%m/%Y %H:%M")


def is_in_future(datetime):
    return datetime > get_current_datetime()


def check_password(psw, hashed_psw):
    if compute_hash(psw) != hashed_psw:
        raise WrongPasswordError("wrong password!")
        

def compute_hash(data):
    hashed_data = hashlib.sha256()
    hashed_data.update(str.encode(data))
    return hashed_data.digest()

############################################
# AUXILIARY FUNCTIONS BELOW (that must be completed and used in the routes)
############################################


def create_reservation(request):
    global _RESERVATIONS, _RESERVATION_ID

    json_data = request.get_json()
   
    _RESERVATIONS[str(_RESERVATION_ID)] = Reservation(_RESERVATION_ID, json_data['name'], json_data['date'], compute_hash(json_data['password']), json_data['guests'])
    

    return jsonify({'reservationid': _RESERVATION_ID})


def get_all_reservations():
    global _RESERVATIONS

    list_of_reservations=list(_RESERVATIONS.values())
    filtered=[]
    for element in list_of_reservations:
        
        if "pytest" in sys.modules:
            date = datetime.strptime(element.serialize()['date'], '%d/%m/%Y %H:%M')
        else:
            date = element.serialize()['date']
        
        if is_in_future(date):
            filtered.append(element.serialize()) 
        
        
    return jsonify({'futurereservations':tuple(filtered)})



############################################
# DO NOT USE
############################################

def set_test_time(datetime_string):
    global _TEST_CLOCK

    if "pytest" not in sys.modules:
        return

    try:
        _TEST_CLOCK=datetime.strptime(datetime_string, '%d/%m/%Y %H:%M')
    except:
        raise WrongDatetimeFormatError(
            "Wrong datetime format. Format is '%d/%m/%Y %H:%M', you sent '{}'".format(datetime_string))


def clear_all():
    global _RESERVATIONS, _RESERVATION_ID
    _RESERVATIONS={}
    _RESERVATION_ID=0
