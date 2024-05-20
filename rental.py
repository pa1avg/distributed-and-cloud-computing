from Pyro5.api import expose, behavior, serve, Daemon
import datetime as dt

@expose
@behavior(instance_mode="single")
class rental(object):
    def __init__(self):
        self.users = [["USER_NAME"], ["USER_CONTACT#"]] # USER TABLE
        self.manufacturers = [["MANUFACTURER"], ["COUNTRY"]] # MANUFACTURER TABLE
        self.available = [["MANUFACTURER"], ["CAR_MODEL"]] # AVAILABLE CARS TABLE
        self.rented = [['USER_NAME'],["USER_CONTACT#"],['MANUFACTURER'],['CAR_MODEL'],['START_DATE'],['END_DATE'],['STATUS'],['KEY']]
                      # RENTED CAR TABLE ( Also treated as historical table with primary key 'KEY')
    
    #Formatting the resultant table
    def resTab(l1,l2):
      max_len = max(len(str(x)) for x in l1)
      sep = '-' * (max_len + 32)
      res = sep + '\n'
      res += f'{"Sl.No.".center(11)} | {l1[0].center(max_len + 1)} | {l2[0].center(max_len)}\n'
      res += sep + '\n'
      for i, (x, y) in enumerate(zip(l1[1:], l2[1:]), start=1):
        res += f'{str(i).center(11)} | {x.ljust(max_len + 2)}| {y}\n'
      res += sep
      return res
    
    #Task 1: Adding user to the system
    def add_user(self,user_name, user_number):
      if user_name not in self.users[0]:
        self.users[0].append(user_name)
        self.users[1].append(user_number)
        print(dt.datetime.now(),': User Added Successfully: {a} | {b}'.format(a = user_name,b=user_number))
      else:
        print(dt.datetime.now(),': User:- "{a}" Already Exists (Failed to Add)'.format(a = user_name))

    #Task 2: Displaying user table to the client
    def return_users(self):
        print(dt.datetime.now(),': Viewed User Table')
        return rental.resTab(self.users[0],self.users[1])

    #Task 3: Adding Manufacturer to the system    
    def add_manufacturer(self, manufacturer_name, manufacturer_country):
      if manufacturer_name not in self.manufacturers[0]:
        self.manufacturers[0].append(manufacturer_name)
        self.manufacturers[1].append(manufacturer_country)
        print(dt.datetime.now(),': Manufacturer Added Successfully: {a} | {b}'.format(a = manufacturer_name,b=manufacturer_country)) 
      else:
        print(dt.datetime.now(),': Manufacturer:- "{a}" Already Exists (Failed to Add)'.format(a = manufacturer_name))

    #Task 4: Displaying Manufacturer table to the client
    def  return_manufacturers(self):
        print(dt.datetime.now(),': Viewed Manufacturer Table')
        return rental.resTab(self.manufacturers[0],self.manufacturers[1])
    
    #Task 5: Adding a car to the system
    def add_rental_car(self, manufacturer_name, car_model):
        if manufacturer_name in self.manufacturers[0]:
            self.available[0].append(manufacturer_name)
            self.available[1].append(car_model)
            print(dt.datetime.now(),': Rental Car Added Successfully: {a} | {b}'.format(a = manufacturer_name,b=car_model))
    
    #Task 6: Displaying available cars table to the client
    def  return_cars_not_rented(self):
        print(dt.datetime.now(),': Viewed Available Cars Table')
        return rental.resTab(self.available[0],self.available[1])

    #Task 7: Renting a car to the user
    def rent_car(self, user_name, car_model, year, month, day):
        if car_model in self.available[1] and day in range(1,32) and month in range(1,13) and len(str(year)) == 4:
            self.rented[0].append(user_name) #uname
            self.rented[1].append(self.users[1][self.users[0].index(user_name)]) #ucontact
            self.rented[2].append(self.available[0][self.available[1].index(car_model)]) #manufacture
            self.rented[3].append(car_model) #car
            self.rented[4].append(dt.datetime(year, month, day)) #sdate
            self.rented[5].append('-')#edate
            self.rented[6].append('RENTED')#status
            self.rented[7].append(str(self.rented[0].count(user_name))+user_name+car_model)#key
            self.available[0].pop(self.available[1].index(car_model))
            self.available[1].remove(car_model)
            print(dt.datetime.now(),': {a} Car Rent Started for {b}'.format(a = car_model,b=user_name))
            return 1
        else:
            return 0    

    #Task 8: Displaying rented cars to the client    
    def return_cars_rented(self):
        man = [self.rented[2][0]]
        car = [self.rented[3][0]]
        print(dt.datetime.now(),': Viewed Rented Cars Table')
        if 'RENTED' in self.rented[6]:
            for i in range(1,len(self.rented[6])):
                if self.rented[6][i] == 'RENTED' and self.rented[5][i] == '-':
                    man.append(self.rented[2][i])
                    car.append(self.rented[3][i])
            return rental.resTab(man,car)
        else:
            return rental.resTab([self.rented[2][0]],[self.rented[3][0]])

    #Task 9: Ending the rental for a user
    def end_rental(self, user_name, car_model, year, month, day):
        ind = self.rented[7].index(str(self.rented[0].count(user_name))+user_name+car_model)
        if self.rented[7][ind] == str(self.rented[0].count(user_name))+user_name+car_model and self.rented[4][ind] <= dt.datetime(year, month, day) and self.rented[-2][ind] == 'RENTED'and day in range(1,32) and month in range(1,13) and len(str(year)) == 4:
            self.available[0].append(self.rented[2][self.rented[3].index(car_model)])
            self.available[1].append(car_model)
            self.rented[5][ind] = dt.datetime(year, month, day)#END DATE
            self.rented[6][ind] = 'NOT RENTED' #CHANGING STATUS
            print(dt.datetime.now(),': {a} Car Rent Ended for {b}'.format(a = car_model,b=user_name))
            return 'Car_Model:- '+self.rented[3][ind]+' ; Name:- '+self.rented[0][ind]+' ; Rented On:- '+str(self.rented[4][ind].date())
        else:
          return 'Enter a Valid User Name/ Car Model/ End Date'

    #Task 10: Delete cars that are not rented currently
    def delete_car(self, car_model):
            if car_model not in self.available[1]:
                print(dt.datetime.now(),': Attempted to delete Car:- {a} from the System - UNSUCCESSFUL'.format(a = car_model))
            while car_model in self.available[1]:
                self.available[0].pop(self.available[1].index(car_model))
                self.available[1].remove(car_model)
            print(dt.datetime.now(),': Attempted to delete Car:- {a} from the System - SUCCESSFUL'.format(a = car_model)) 

    #Task 11: Delete user who did not rent previously
    def delete_user(self, user_name):
        if user_name not in self.rented[0]:
            self.users[1].pop(self.users[0].index(user_name))
            self.users[0].remove(user_name)
            print(dt.datetime.now(),': Attempted to delete User:- {a} from the System - SUCCESSFUL'.format(a = user_name))
            return 1
        else:
            print(dt.datetime.now(),': Attempted to delete User:- {a} from the System - UNSUCCESSFUL'.format(a = user_name))
            return 0

    #Task 12: Displaying rental history of a user to the client
    def user_rental_date(self, user_name, start_year, start_month, start_day, end_year,end_month, end_day):
      reslst = [[self.rented[2][0]], [self.rented[3][0]]]
      sd = dt.datetime(start_year,start_month,start_day)
      ed = dt.datetime(end_year,end_month,end_day)
      print(dt.datetime.now(),': Viewed Rental History for {a} from {b} to {c}'.format(a=user_name,b=sd.date(),c=ed.date()))
      for i in range(1,len(self.rented[0])):
        if (self.rented[0][i] == user_name and self.rented[5][i] != '-' and sd <= self.rented[4][i] <= ed and sd <= self.rented[5][i] <= ed):
          reslst[0].append(self.rented[2][i])
          reslst[1].append(self.rented[3][i])
      return rental.resTab(reslst[0],reslst[1])
      
daemon = Daemon() 
serve({rental: "example.rental"}, daemon=daemon, use_ns=True)