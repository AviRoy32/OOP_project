# entities: Book,user,library
# functionalities: add user,add book,borrow,return

class Book:
    def __init__(self,catagory,id,name,quantity):
        self.catagory = catagory 
        self.id = id
        self.name = name
        self.quantity = quantity

class User:
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBooks = []
        self.returnBooks = []

class Library:
    def __init__(self,owner,name):
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []

    def addBook(self,catagory,id,name,quantity):
        book = Book(catagory,id,name,quantity)
        self.books.append(book)
        print(f"\n\t{name} Books added successfully ! ")

    def addUser(self,id,name,password):
        user = User(id,name,password)
        self.users.append(user)
        return user

    def borrowBook(self,user,id):
        for book in self.books:    #library te boi ta ase kina
            if book.id==id:
                if book in user.borrowedBooks:
                    print("\n\tAlready Borrowed ! ")
                    return
                elif book.quantity < 1:
                    print("\n\tNo Available copies ! ")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity-=1
                    print(f"\n\t{book.name} borrowed successfully ! ")
                    return

        print("\n\tBook Not found !")

    def returnBook(self,user,id):
        for book in user.borrowedBooks:
            if book.id==id:
                user.borrowedBooks.remove(book)
                user.returnBooks.append(book)
                book.quantity+=1
                print(f"\n\t{book.name} returned successfully ! ")
                return
        print(f"{book.name} not found in borrowed list! ")

    def showUsers(self):
        print("\n\tAvailable users: ")
        for user in self.users:
            print(f"\n\tID: {user.id}, Name: {user.name}")

    def showBooks(self):
        print("\nAvailable Books: ")
        for book in self.books:
            print(f"\tID: {book.id},Name: {book.name},quantity: {book.quantity}")


    
pl=Library("Avi Roy","PUST")
admin = pl.addUser(101,"admin",1234)
avi = pl.addUser(102,"Avi",6789)
pybook = pl.addBook("science",1,"javatpoint",10)


run = True
currentUser=admin
while run:
    if currentUser == None:
        print(f"\n\tNo logged in user ! ")

        option = input("Login ? Registration (L/R): ")
        if option=='R':
            id=int(input("\tEnter id: "))
            name=input("\tEnter Name: ")
            password=input("\tEnter Password: ")

            user=pl.addUser(id,name,password)
            currentUser=user

        elif option=='L':
           id=int(input("\tEnter id: ")) 
           password=input("\tEnter Password: ")

           match=False
           for user in pl.users:
               if user.id==id and user.password==password:
                    currentUser=user
                    match=True
                    break

           if match==False:
                print(f"\n\tNo user found ! ")

    else:
        if currentUser.name=='admin':
            print("Options: \n")

            print("1 : Add Book")    
            print("2 : show users")    
            print("3 : show Book")    
            print("4 : Logout") 

            ch=int(input("\nEnter option: "))

            if ch==1:
                cat=input("\tEnter catagory: ")   
                id=int(input("\tEnter id: "))  
                name=input("\tEnter Name: ")   
                quantity=int(input("\tEnter quantity: ")) 

                pl.addBook(cat,id,name,quantity)

            elif ch==2:
                pl.showUsers() 

            elif ch==3:
                pl.showBooks()

            elif ch==4:
                currentUser=None
        
        else:
            print("Options: \n")

            print("1 : Borrow Book")
            print("2 : Return Book")
            print("3 : show Books")
            print("4 : show Borrowed Books")
            print("5 : show Returned Books")
            print("6 : Logout")
            print("7 : Exit")

            ch=int(input("\nEnter option: "))
            if ch==1:
                id=int(input("\tEnter id: "))
                pl.borrowBook(currentUser,id)

            elif ch==2:
                id = int(input("\tEnter id: "))
                pl.returnBook(currentUser, id)


            elif ch==3:
                pl.showBooks()

            elif ch==4:
                print("\n\tBorrowed Books: ")
                for book in currentUser.borrowedBooks:
                    print(f"\tID: {book.id}, Name: {book.name}")

            elif ch==5:
                print("\tReturned Books: ")
                for book in currentUser.returnBooks:
                    print(f"\tID: {book.id}, Name: {book.name}")

            elif ch==6:
                currentUser=None

            elif ch == 7:
                run = False
                print("\nExiting the program. Goodbye!")



