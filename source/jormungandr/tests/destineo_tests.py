# Copyright (c) 2001-2014, Canal TP and/or its affiliates. All rights reserved.
#
# This file is part of Navitia,
#     the software to build cool stuff with public transport.
#
# Hope you'll enjoy and contribute to this project,
#     powered by Canal TP (www.canaltp.fr).
# Help us simplify mobility and open public transport:
#     a non ending quest to the responsive locomotion way of traveling!
#
# LICENCE: This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Stay tuned using
# twitter @navitia
# IRC #navitia on freenode
# https://groups.google.com/d/forum/navitia
# www.navitia.io

from nose.tools import eq_

from jormungandr.scenarios import destineo
import navitiacommon.response_pb2 as response_pb2
from jormungandr.utils import str_to_time_stamp

def is_pure_tc_simple_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert destineo.is_pure_tc(journey)

def is_pure_tc_bss_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey.sections.add()
    section.type = response_pb2.BSS_RENT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section = journey.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert not destineo.is_pure_tc(journey)


def is_pure_tc_crowfly_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.CROW_FLY
    section.street_network.mode = response_pb2.Walking
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert destineo.is_pure_tc(journey)


def has_bike_and_tc_simple_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert not destineo.has_bike_and_tc(journey)

def has_bike_and_tc_bss_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey.sections.add()
    section.type = response_pb2.BSS_RENT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section = journey.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert not destineo.has_bike_and_tc(journey)


def has_bike_and_tc_crowfly_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.CROW_FLY
    section.street_network.mode = response_pb2.Bike
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert destineo.has_bike_and_tc(journey)

def has_bss_and_tc_simple_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert not destineo.has_bss_and_tc(journey)

def has_bss_and_tc_bss_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey.sections.add()
    section.type = response_pb2.BSS_RENT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section = journey.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert destineo.has_bss_and_tc(journey)


def has_bss_and_tc_crowfly_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.CROW_FLY
    section.street_network.mode = response_pb2.Bike
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert not destineo.has_bss_and_tc(journey)

def has_bss_and_tc_crowfly_bss_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.CROW_FLY
    section.street_network.mode = response_pb2.Bss
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert not destineo.has_bss_and_tc(journey)

def has_car_and_tc_simple_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert not destineo.has_car_and_tc(journey)

def has_car_and_tc_bss_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey.sections.add()
    section.type = response_pb2.BSS_RENT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section = journey.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert not destineo.has_car_and_tc(journey)


def has_car_and_tc_crowfly_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.CROW_FLY
    section.street_network.mode = response_pb2.Car
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert destineo.has_car_and_tc(journey)

def has_car_and_tc_crowfly_bss_test():
    response = response_pb2.Response()
    journey = response.journeys.add()

    journey.type = "best"
    section = journey.sections.add()
    section.type = response_pb2.CROW_FLY
    section.street_network.mode = response_pb2.Bss
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    assert not destineo.has_car_and_tc(journey)

def sort_destineo_test():
    response = response_pb2.Response()

    journey_tc3 = response.journeys.add()
    journey_tc3.type = "rapid"
    journey_tc3.departure_date_time = str_to_time_stamp('20141103T123000')
    section = journey_tc3.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey_tc3.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey_tc3.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    journey_tc1 = response.journeys.add()
    journey_tc1.type = "rapid"
    journey_tc1.departure_date_time = str_to_time_stamp('20141103T110000')
    section = journey_tc1.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey_tc1.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey_tc1.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    journey_bike = response.journeys.add()
    journey_bike.type = "non_pt_bike"

    journey_bss = response.journeys.add()
    journey_bss.type = "non_pt_bss"
    section = journey_bss.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey_bss.sections.add()
    section.type = response_pb2.BSS_RENT
    section = journey_bss.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section = journey_bss.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section = journey_bss.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    journey_walk = response.journeys.add()
    journey_walk.type = "non_pt_walk"

    journey_tc2 = response.journeys.add()
    journey_tc2.type = "rapid"
    journey_tc2.departure_date_time = str_to_time_stamp('20141103T120000')
    section = journey_tc2.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey_tc2.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey_tc2.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    journey_bss_and_tc = response.journeys.add()
    journey_bss_and_tc.type = "rapid"
    section = journey_bss_and_tc.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section = journey_bss_and_tc.sections.add()
    section.type = response_pb2.BSS_RENT
    section = journey_bss_and_tc.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section = journey_bss_and_tc.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section = journey_bss_and_tc.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey_bss_and_tc.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    journey_bike_and_tc = response.journeys.add()
    journey_bike_and_tc.type = "rapid"
    section = journey_bike_and_tc.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section = journey_bike_and_tc.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey_bike_and_tc.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    journey_car_and_tc = response.journeys.add()
    journey_car_and_tc.type = "rapid"
    section = journey_car_and_tc.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Car
    section = journey_car_and_tc.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section = journey_car_and_tc.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking

    scenario = destineo.Scenario()
    scenario._custom_sort_journeys(response)
    eq_(response.journeys[0], journey_tc1)
    eq_(response.journeys[1], journey_tc2)
    eq_(response.journeys[2], journey_tc3)
    eq_(response.journeys[3], journey_bss)
    eq_(response.journeys[4], journey_bss_and_tc)
    eq_(response.journeys[5], journey_bike_and_tc)
    eq_(response.journeys[6], journey_car_and_tc)
    eq_(response.journeys[7], journey_walk)
    eq_(response.journeys[8], journey_bike)



def bike_duration_walking_test():
    journey = response_pb2.Journey()

    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60

    eq_(destineo.bike_duration(journey), 0)

def bike_duration_bike_test():
    journey = response_pb2.Journey()

    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 70

    eq_(destineo.bike_duration(journey), 130)


def bike_duration_bss_test():
    journey = response_pb2.Journey()

    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 30
    section = journey.sections.add()
    section.type = response_pb2.BSS_RENT
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 120
    section = journey.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 5

    eq_(destineo.bike_duration(journey), 5)

def car_duration_walking_test():
    journey = response_pb2.Journey()

    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60

    eq_(destineo.car_duration(journey), 0)

def car_duration_car_test():
    journey = response_pb2.Journey()

    section = journey.sections.add()
    section.type = response_pb2.LEAVE_PARKING
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Car
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PARK
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 70

    eq_(destineo.car_duration(journey), 60)


def car_duration_bss_test():
    journey = response_pb2.Journey()

    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 30
    section = journey.sections.add()
    section.type = response_pb2.BSS_RENT
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 120
    section = journey.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.LEAVE_PARKING
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Car
    section.duration = 180
    section = journey.sections.add()
    section.type = response_pb2.PARK
    section.duration = 10

    eq_(destineo.car_duration(journey), 180)

def tc_duration_walking_test():
    journey = response_pb2.Journey()

    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60

    eq_(destineo.tc_duration(journey), 80)

def tc_duration_bike_test():
    journey = response_pb2.Journey()

    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.TRANSFER
    section.duration = 20
    section = journey.sections.add()
    section.type = response_pb2.WAITING
    section.duration = 25
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 40
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 70

    eq_(destineo.tc_duration(journey), 120)


def tc_duration_bss_test():
    journey = response_pb2.Journey()

    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 30
    section = journey.sections.add()
    section.type = response_pb2.BSS_RENT
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 120
    section = journey.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 5

    eq_(destineo.tc_duration(journey), 80)

class Instance(object):
    def __init__(self):
        self.destineo_min_bike = 30
        self.destineo_min_car = 20
        self.destineo_min_tc_with_bike = 40
        self.destineo_min_tc_with_car = 50

def remove_not_long_enough_no_removal_test():
    response = response_pb2.Response()

    journey = response.journeys.add()
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60

    journey = response.journeys.add()
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.BSS_RENT
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 120
    section = journey.sections.add()
    section.type = response_pb2.BSS_PUT_BACK
    section.duration = 10
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60

    scenario = destineo.Scenario()
    scenario._remove_not_long_enough_fallback(response.journeys, Instance())
    eq_(len(response.journeys), 2)
    scenario._remove_not_long_enough_tc_with_fallback(response.journeys, Instance())
    eq_(len(response.journeys), 2)


def remove_not_long_enough_bike():
    response = response_pb2.Response()

    journey = response.journeys.add()
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60

    journey2 = response.journeys.add()
    section = journey2.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey2.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey2.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 29

    journey3 = response.journeys.add()
    section = journey3.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey3.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 39
    section = journey3.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 30

    journey4 = response.journeys.add()
    section = journey4.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey4.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 40
    section = journey4.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Bike
    section.duration = 30

    scenario = destineo.Scenario()
    scenario._remove_not_long_enough_fallback(response.journeys, Instance())
    eq_(len(response.journeys), 3)
    eq_(response.journeys[0], journey)
    eq_(response.journeys[1], journey3)
    eq_(response.journeys[2], journey4)
    scenario._remove_not_long_enough_tc_with_fallback(response.journeys, Instance())
    eq_(len(response.journeys), 2)
    eq_(response.journeys[0], journey)
    eq_(response.journeys[1], journey4)


def remove_not_long_enough_car():
    response = response_pb2.Response()

    journey = response.journeys.add()
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60

    journey2 = response.journeys.add()
    section = journey2.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey2.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 80
    section = journey2.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Car
    section.duration = 19

    journey3 = response.journeys.add()
    section = journey3.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey3.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 49
    section = journey3.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Car
    section.duration = 20

    journey4 = response.journeys.add()
    section = journey4.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Walking
    section.duration = 60
    section = journey4.sections.add()
    section.type = response_pb2.PUBLIC_TRANSPORT
    section.duration = 50
    section = journey4.sections.add()
    section.type = response_pb2.STREET_NETWORK
    section.street_network.mode = response_pb2.Car
    section.duration = 20

    scenario = destineo.Scenario()
    scenario._remove_not_long_enough_fallback(response.journeys, Instance())
    eq_(len(response.journeys), 3)
    eq_(response.journeys[0], journey)
    eq_(response.journeys[1], journey3)
    eq_(response.journeys[2], journey4)
    scenario._remove_not_long_enough_tc_with_fallback(response.journeys, Instance())
    eq_(len(response.journeys), 2)
    eq_(response.journeys[0], journey)
    eq_(response.journeys[1], journey4)
