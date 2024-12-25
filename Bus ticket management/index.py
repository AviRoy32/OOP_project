from abc import ABC,abstractmethod

class AbstractBus(ABC):
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seats = ["Empty" for _ in range(20)]
        
    # @abstractmethod
    # def instal_bus(self,coach,driver,arrival,departure,from_des,to):
    #     pass

    # @abstractmethod
    # def display_available_buses(self):
    #     pass

    # @abstractmethod
    # def display_seat_status(self):
    #     pass

class Bus(AbstractBus):
    # def instal_bus(coach, driver, arrival, departure, from_des, to):
    #     print(f"Bus {coach} installed successfully!")
    pass

class BusCompany:
    def __init__(self):
        self.buses = {}  #sokol bus er details takbe.database hisebe kaj

    def install_bus(self,bus):
        print(f"Bus {bus.coach} added successfully!!")
        self.buses[bus.coach] = bus

    def display_available_buses(self):
        if not self.buses:
            print("No Buses are available!!")
        else:
            print(f"Coach\tDriver\tArrival\tDeparture\tfrom_des\tto")
            for coach,bus in self.buses.items():
                print(f"{coach}\t{bus.driver}\t{bus.arrival}\t{bus.departure}\t{bus.from_des}\t{bus.to}")


    def book_ticket(self,coach,seat):
        if coach in self.buses:
            if 1<=seat<=20:
                if self.buses[coach].seats[seat-1] == 'Empty':
                    print("seat Booked Successfully!!")
                    self.buses[coach].seats[seat-1] = 'Booked'
                else:
                    print("Seat already booked!!")
            else:
                print("Invalid seat number!!")
        else:
            print("Invalid bus coach number!!")

    def display_seat_status(self,coach):
         if coach in self.buses:
             print(self.buses[coach].seats)


company = BusCompany()


while True:
    print("WElcome to Bus Ticket Booking system!!!")
    print("1. Install Bus")
    print("2. View available Bus")
    print("3. Book Ticket")
    print("4. check seat status")
    print("5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        coach = input("Enter Bus number: ")
        driver = input("Enter Bus driver name: ")
        arrival = input("Enter Bus arrival time: ")
        departure = input("Enter Bus departure time: ")
        from_des = input("Enter Bus from destination: ")
        to = input("Enter Bus to destination: ")
        bus = Bus(coach,driver,arrival,departure,from_des,to)
        company.install_bus(bus)

    elif choice == 2:
        company.display_available_buses()

    elif choice == 3:
        coach = input("Enter Bus number: ")
        seat = int(input("Enter seat number: "))
        company.book_ticket(coach,seat)

    elif choice == 4:
        coach = input("Enter bus number: ")
        company.display_seat_status(coach)

    elif choice == 5:
        print("Thanks for using our service!!")
        break

    else:
        print("Invalid choice")
