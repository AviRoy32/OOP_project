from abc import ABC,abstractmethod
from ride import RideRequest,RideMatching,RideSharing

class User(ABC):
    def __init__(self,name,email,id):
        self.name = name
        self.email = email
        self.id = id

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, id, current_location, initial_amount):
        super().__init__(name, email, id)
        self.current_ride = None
        self.current_location = current_location
        self.wallet = initial_amount

    def display_profile(self):
        print(f"Rider : {self.name} and email : {self.email}")

    def load_cash(self,amount):
        if amount > 0:
            self.wallet+=amount
        else:
            print("Amount less than 0")

    def update_location(self,current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = RideRequest(self,destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request,vehicle_type)
        ride.rider = self
        self.current_ride = ride
        print("Yes,we got a ride")

    def show_current_ride(self):
        print("Ride Details")
        print(f"Rider : {self.name}")
        print(f"Driver :{self.current_ride.driver.name}")
        print(f"selected car :{self.current_ride.vehicle.vehicle_type}")
        print(f"start location :{self.current_ride.start_location}")
        print(f"End location :{self.current_ride.end_location}")
        print(f"Total Cost :{self.current_ride.estimated_fare}")


class Driver(User):
    def __init__(self, name, email, id,current_location):
        super().__init__(name, email, id)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f"Driver Name : {self.name}")

    def accept_ride(self,ride):
        #accept korbo
        ride.start_ride()
        ride.set_driver(self)

    def reach_destination(self,ride):
        ride.end_ride()


