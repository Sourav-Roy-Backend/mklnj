#Bus Ticket Booking System

#Admin -
# 1) Add a new bus
# 2) Cheack available buses
# 3) Can check bus info

#User
# 1) Cheack available buses
# 2) can check bus info
# 3)can reserve sea


class user:
    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password

class bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.from_des=from_des
        self.to=to
        self.departure=departure
        self.seat=["empty" for i in range(20)]
# b=bus(2,"Liyon","12 pm","3 pm","dinajpur","rangpur")
# print(vars(b))

class phitron:
    user_list=[]
    total_bus=5
    total_bus_list=[]

    def add_bus(self):
        bus_no=int(input("Enter Bus no : "))

        flag=1
        for w in self.total_bus_list:
        
            if bus_no == w['coach']:
                print("bus alredy added")
                flag=0
                break
        if flag:
                bus_driver=input("Enter bus driver name : ")
                bus_arrival=input("Enter Bus Arrival Time : ")
                bus_departure=input("Enter Bus Departure Time : ")
                bus_from=input("Enter Bus Start From : ")
                bus_to=input("Enter Bus Destination : ")
                self.new_bus=bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
                self.total_bus_list.append(vars(self.new_bus))
                print("\n Bus Added Succesfully")
# company=phitron()
# company.add_bus()

class counter(phitron):
    def reservation(self):
        bus_no=int(input("Enter Bus no : "))

        for w in self.total_bus_list:
            if bus_no == w['coach']:
                passeger=input("Enter your name : ")
                seat_no=int(input("Enter seat no : "))

                if seat_no>20:
                    print("no seats available !!")
                elif w['seat'][seat_no-1]!="empty":
                    print("seat Alredy booked")
                else:
                    w['seat'][seat_no-1]=passeger
            else:
                print("NO bus avilable")

#         for bus in self.total_bus_list:
#             print(bus['seat'])

    def show_ticket(self):
            bus_no=int(input("Enter Bus Number : "))

            for w in self.total_bus_list:
                if bus_no == w['coach']:
                    print('*'*50)
                    print()
                    print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                    print(f"BUS NUMBER : {bus_no}\t\t\t Driver:{w['driver']}")
                    print(f"Arival:{w['arrival']}\t\t\t Departure Time :{w['departure']} \n From : {w['from_des']} \t\t\t  To: \t{w['to']}")
                    print()
                    
                    a=1
                    for i in range(5):
                        for j in range(2):
                            print(f"{a}. {w['seat'][a-1]}",end="\t")
                            a+=1
                        for k in range(2):
                            print(f"{a}. {w['seat'][a-1]}",end="\t")
                            a+=1
                        print()
                    print('*'*50)

    def get_user(self):
        return self.user_list
    
    def create_account(self):
        name=input("Enter your username : ")
        password=input("Enter your password : ")
        self.new_user=user(name,password)
        self.user_list.append(vars(self.new_user))

    def available_buses(self):
        if len(self.total_bus_list)==0:
            print("NO Buses Available\n")
        else:
            print('*'*50)
            for bus in self.total_bus_list:
                print()
                print(f"{' '*10}{'#'*10} Bus {bus['coach']} INFO {'#'*10}")
                print(f"Bus number : {bus['coach']} \t Driver : {bus['driver']}")
                print(f"Arrival :{bus['arrival']} \t departure time :{bus['departure']} \n From:\t {bus['from_des']} \t\t To {bus['to']}")
            print('*'*50)


# company=phitron()
# company.add_bus()

# c=counter()
# c.reservation()

while True:
    company=phitron()
    b=counter()
    print("1.Create an account \n2.Login to your account \n3.Exit")

    user_input=int(input("Enter your choice :"))
    if user_input==3:
        break
    elif user_input==1:
        b.create_account()
    elif user_input==2:
        name=input("Enter your name : ")
        password=input("Enter your password : ")

        flag=0
        isadmin=False

        if name=="admin" and password=="123":
            isadmin=True
        if isadmin==False:
            for User in b.get_user():
                if User['username']==name and User['password']==password:
                    flag=1
                    break
            if flag:
                while True:
                    print(f"\n{' '*10}Welcome to bus ticket booking system")
                    print("1.Availble Buses \n2.Show bus info \n3.Resevation\n4.Exit")
                    a=int(input("Enter your choice : "))
                    if a== 4:
                        break
                    elif a==1:
                        b.available_buses()
                    elif a==2:
                        b.show_ticket()
                    elif a==3:
                        b.reservation()
            else:
                print("No username Found")
        else:
            while True:
                print(f"\n{' '*10} Hello admin welcome to bus ticket system ")
                print("1.Add Bus \n2.Avilable Bus \n3.show bus info \n4.Exit")
                a=int(input("Enter your choice : "))
                if a==4:
                    break
                elif a==1:
                    b.add_bus()
                elif a==2:
                    b.available_buses()
                elif a==3:
                    b.show_ticket()
                





#Global
    # 1.create an create_account
    # 2.login to your account 
    # 3.exit

    # user 
    #     1.Bus info
    #     2.beserve/ticket booking
    #     3.available_buses
    #     4.exit
    # admin
    #     1.add bus 
    #     2.avilable bus 
    #     3.can check bus info
    #     4.exit


    
