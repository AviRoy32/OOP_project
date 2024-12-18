class Star_Cinema:
    hall_list = []

    def entry_hall(self,hall):
        self.hall_list.append(hall)  

    def get_hall_list(self):
        return self.hall_list
    

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        super().__init__()
        self.__seats = {}
        self.__showlist = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        self.entry_hall(self)

    def entry_show(self,id,movie_name,time):
        self.__showlist.append((id,movie_name,time))
        self.__seats[id] = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]


    def bookSeats(self,show_id,seat_list):
        if show_id not in self.__seats:
            print("\n\t Invalid show ID  ! ")
            return
        
        for row,col in seat_list:
            if row<0 or row>=self.__rows or col<0 or col>=self.__cols:
                print(f"\n\t seat ({row}{col}) is invalid ! ")
                return
            elif self.__seats[show_id][row][col] != "Free":
                print(f"\n\tseat ({row}{col}) already booked ! ")
                return
            
        for row,col in seat_list:
            self.__seats[show_id][row][col] = "Booked"
        print(f"\n\tseat {seat_list} booked for {show_id} ")  


    def view_show_list(self):
        print(f"\n\tshows Running in hall {self.__hall_no}")
        for movie_id,movie_name,time in self.__showlist:
            print(f"\n\tID: {movie_id}, Movie: {movie_name}, Time: {time}")


    def view_available_seats(self,show_id):
        if show_id not in self.__seats:
            print("\n\t Invalid show ID  ! ")
            return
        
        print(f"\nAvailable seats for {show_id} in hall {self.__hall_no}")
        for row in range(self.__rows):
            for col in range(self.__cols):
                status=self.__seats[show_id][row][col]
                print(f"({row},{col}):{status}", end="\t")   
            print()  


#replica
Rupkotha = Hall(5,5,101)
entry1 = Rupkotha.entry_show(1001,"Jawan","18/12/2024   3:00 PM")
entry2 = Rupkotha.entry_show(1002,"Lucky vaskar","18/12/2024   6:00 PM")
entry3 = Rupkotha.entry_show(1003,"Dewana","18/12/2024   9:00 PM")

while True:
    print("counter options: ")
    print("1.VIEW ALL SHOW TODAY: ")
    print("2.VIEW AVAILABLE SEATS: ")
    print("3.BOOK TICKET: ")
    print("4.EXIT: ")

    ch=int(input("Enter choice: "))

    if ch==1:
        for hall in Rupkotha.get_hall_list():
            hall.view_show_list()

    elif ch==2:
        id = int(input("Enter show id: "))
        Rupkotha.view_available_seats(id)

    elif ch==3:
        id=int(input("Enter show id: "))
        number_of_seats=int(input("Enter total seat: "))
        seat=[]

        for _ in range(number_of_seats):
            row = int(input("Enter Row: "))
            col = int(input("Enter column: "))
            seat.append((row,col))

        Rupkotha.bookSeats(id,seat)

    elif ch==4:
        print("Exit ")
        break

    else:
        print("Invalid option! please input correct option.")

