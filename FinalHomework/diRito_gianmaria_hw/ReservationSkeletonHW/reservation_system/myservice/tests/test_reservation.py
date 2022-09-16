import unittest
import json
from flask import request, jsonify
from myservice.views.reservations import set_test_time, get_current_datetime, clear_all
from myservice.app import app as tested_app


class TestApp(unittest.TestCase):

    def setUp(self):
        app = tested_app.test_client()
        set_test_time("01/04/2020 10:30")

        
        # no loaded reservation 
        reply = app.get('/reservations/count')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body['nreservations'], 0)

        # create 3 reservations 
        reply = app.post('/reservations',
                         data=json.dumps({
                             "name" : "Stefano",
                             "password" : "ciaone",
                             "date" : "01/04/2020 20:30",
                             "guests": ["Remo", "Davide"],
                         }),
                         content_type='application/json')

        body = json.loads(str(reply.data, 'utf8'))

        self.assertEqual(body['reservationid'], 0)

        reply = app.post('/reservations',
                         data=json.dumps({
                            "name" : "Antonio",
                             "password" : "password",
                             "date" : "01/04/2020 22:30",
                             "guests": [],
                         }),
                         content_type='application/json')

        body = json.loads(str(reply.data, 'utf8'))

        self.assertEqual(body['reservationid'], 1)

        reply = app.post('/reservations',
                         data=json.dumps({
                             "name" : "Franco",
                             "password" : "franco",
                             "date" : "01/04/2020 12:30",
                             "guests": ["Carlo", "Chiara"],
                         }),
                         content_type='application/json')

        body = json.loads(str(reply.data, 'utf8'))

        self.assertEqual(body['reservationid'], 2)

    def tearDown(self):
        clear_all()


    def test_create_reservations(self):
        app = tested_app.test_client()

        # get the number of future reservations 
        reply = app.get('/reservations/count')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body['nreservations'], 3)

        # time passes
        set_test_time("01/04/2020 14:00")

        # get the number of future reservations
        reply = app.get('/reservations/count')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body['nreservations'], 2)


    def test_retrieve_reservations(self):
        app = tested_app.test_client()

        #get the second reservation 
        reply = app.get('/reservation/1')
        body = json.loads(str(reply.data, 'utf8'))
        assertion = { "reservation" :
                                    {
                                        "id" : 1,
                                        "name" : "Antonio",
                                        "date" : "01/04/2020 22:30",
                                        "guests" : []
                                    }
                                }
        self.assertEqual(body, assertion)

        #time passed 
        set_test_time("01/04/2020 15:30")

        # get future reservations
        reply = app.get('/reservations')
        body = json.loads(str(reply.data, 'utf8'))
        assertion =  {
            "futurereservations": [
                {
                    "id" : 0,
                    "name" : "Stefano",
                    "date" : "01/04/2020 20:30",
                    "guests" : ["Remo", "Davide"],
                },
                {
                    "id" : 1,
                    "name" : "Antonio",
                    "date" : "01/04/2020 22:30",
                    "guests" : [],
                },
            ]
        }

        self.assertEqual(body, assertion)

        #try to retrieve a non-existing reservation 
        reply = app.get('/reservation/100')
        self.assertEqual(reply.status_code, 404)

    def test_delete_reservations(self):
        app = tested_app.test_client()

        # delete a reservation
        reply = app.delete('/reservation/0',
                         data=json.dumps({
                             "password" : "ciaone"
                         }),
                         content_type='application/json')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body["reservationid"], '0')

        #try to retrieve the deleted reservation
        reply = app.get('/reservation/0')
        self.assertEqual(reply.status_code, 410)

        
        # attempt deleting a reservation with wrong password
        reply = app.delete('/reservation/1',
                         data=json.dumps({
                             "password" : "a_wrong_psw"
                         }),
                         content_type='application/json')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body["error"], 'wrong password')


        # attempt deleting a past reservation

        # time passed 
        set_test_time("01/04/2020 23:30")

        reply = app.delete('/reservation/1',
                         data=json.dumps({
                             "password" : "password"
                         }),
                         content_type='application/json')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body["error"], 'past reservation')



    def test_guests(self):
        app = tested_app.test_client()
        
        # check number of guests
        reply = app.get('/reservation/1/guests')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body["nguests"], 0)


        # change the list of guests
        new_guests = ["Lucia", "Elisabetta"]
        reply = app.put('/reservation/1/guests',
                         data=json.dumps({
                            "guests": new_guests,
                            "password": "password"
                         }),
                         content_type='application/json')

        body = json.loads(str(reply.data, 'utf8'))

        self.assertEqual(body['guests'], new_guests)


        # attempt changing list of guests with wrong password
        new_guests = ["Filippa", "Paolino"]
        reply = app.put('/reservation/1/guests',
                         data=json.dumps({
                            "guests": new_guests,
                            "password": "random_psw"
                         }),
                         content_type='application/json')

        body = json.loads(str(reply.data, 'utf8'))

        self.assertEqual(body['error'], "wrong password")

        # attempt changing list of guests of past reservation

        # time passed 
        set_test_time("01/04/2020 23:30")

        new_guests = ["Lucia", "Elisabetta"]
        reply = app.put('/reservation/1/guests',
                         data=json.dumps({
                            "guests": new_guests,
                            "password": "password"
                         }),
                         content_type='application/json')

        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body["error"], 'past reservation')
        
