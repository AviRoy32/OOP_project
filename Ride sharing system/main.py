from ride import Ride,RideMatching,RideRequest,RideSharing
from users import Rider,Driver
from vehicle import Car,Bike

niye_jao = RideSharing("Niye jao")
rahim = Rider("Rahim uddin","rahim@gmail.com",1234,"mohakhali",1200)
niye_jao.add_rider(rahim)
kolom = Driver("kolim","kolim@gmail.com",435,"gulshan")
niye_jao.add_driver(kolom)
rahim.request_ride(niye_jao,"uttara","car")

kolom.reach_destination(rahim.current_ride)
rahim.show_current_ride()
# print(niye_jao)