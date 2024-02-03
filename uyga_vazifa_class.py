
# problem 3

# class Shaxs:
#     def __init__(self,ism: str, familiya: str, yosh: int, oylik_daromad: int):
#         self.ism=ism
#         self.familiya=familiya
#         self.yosh=yosh
#         self.oylik_daromad=oylik_daromad
#     def info(self):
#         return f"""
# ism: {self.ism}
# familiya: {self.familiya}
# yosh: {self.yosh}
# oylik_daromad: {self.oylik_daromad}
# soliq: {self.soliq}    
#     """
    
# class Talaba(Shaxs):
#     def __init__(self,ism: str, familiya: str, yosh: int, oylik_daromad: int,soliq: int):
#         super().__init__(ism,familiya,yosh,oylik_daromad)
#         self.soliq=soliq
        
# class Ishchi(Shaxs):
#     def __init__(self,ism: str, familiya: str, yosh: int, oylik_daromad: int,soliq: int):
#         super().__init__(ism,familiya,yosh,oylik_daromad)
#         self.soliq=soliq
# class Pinsioner(Shaxs):
#     def __init__(self,ism: str, familiya: str, yosh: int, oylik_daromad: int,soliq: int):
#         super().__init__(ism,familiya,yosh,oylik_daromad)
#         self.soliq=soliq
        
# print("\tTALABALAR: ")
# talaba1=Talaba("asror","kenjayev",17,5000000,223000)
# talaba2=Talaba("eldor","mirzaqulov",18,6000000,330000)
# print(talaba1.info())
# print(talaba2.info())

# print("\tISHCHILAR: ")
# ishchi1=Ishchi("sardor","beknazarov",25,12000000,340000)
# ishchi2=Ishchi("nazar","hayitov",32,13000000,345000)
# print(ishchi1.info())
# print(ishchi2.info())

# print("\tPINSIONERLAR:")
# pinsioner1=Pinsioner("davlat","qurbonov",97,2300000,120000)
# pinsioner2=Pinsioner("holmat","eshmatov",76,2300000,120000)
# print(pinsioner1.info())
# print(pinsioner2.info())



# problem 2
# class Uy:
#     def __init__(self,type: str, sum_room: int, area: int, price: int):
#         self.type=type
#         self.sum_room=sum_room
#         self.area=area
#         self.price=price
    
    
# class Flat(Uy):
#     def __init__(self,type: str, sum_room: int, area: int, price: int,location: str,condition: str):
#         super().__init__(type,sum_room,area,price)
#         self.location=location
#         self.condition=condition
#     def set_price(self,new_price):
#         self.price=new_price

#     def info(self):
#         return f"""
# type: {self.type}
# sum_room: {self.sum_room}ta xona 
# area: {self.area}kv
# price: {self.price}$
# location: {self.location}da
# condition: {self.condition}
# """

# class House(Uy):
#     def __init__(self,type: str, sum_room: int, area: int, price: int,location: str,condition: str):
#         super().__init__(type,sum_room,area,price)
#         self.location=location
#         self.condition=condition
#     def set_price(self,new_price):
#         self.price=new_price
#     def info(self):
#         return f"""
# type: {self.type}
# sum_room: {self.sum_room}ta xona 
# area: {self.area}kv
# price: {self.price}$
# location: {self.location}da
# condition: {self.condition}
# """

# flat1=Flat("dom",3,60,30000,"chilonzor","yangi")
# flat2=Flat("dom",2,45,20000,"yunusobod","yaxshi")
# flat3=Flat("dom",5,120,55000,"chilonzor","yangi uy")

# flat1.set_price(40000)
# flat2.set_price(25000)
# flat3.set_price(42000)

# lst=[flat1,flat2,flat3]
# max_price=max(lst,key=lambda x:x.price)
# print(max_price.info())

# house1=House("hovli",6,600,1000000,"yakkasaroy","yangi hovli")
# house2=House("hovli",5,600,900000,"qatartol","yangi hovli")
# house3=House("hovli",6,600,980000,"chilonzor","yangi hovli")

# house1.set_price(1200000)
# house2.set_price(920000)
# house3.set_price(1000000)

# lst=[house1,house2,house3]
# max_price=max(lst,key=lambda uy:uy.price)
# print(max_price.info())


# problem 1
# class Animal:
#     def __init__(self,animal_type: str, color: str, long_age: int):
#         self.animal_type=animal_type
#         self.color=color
#         self.long_age=long_age
#     def info(self):
#         return f"""
#  animal_type: {self.animal_type}
#  color: {self.color}
#  long_age: {self.long_age}
#  high_speed: {self.high_speed}
#  sum_teeth: {self.sum_teeth}
    
#     """
        
# class Dog(Animal):
#     def __init__(self,animal_type: str, color: str, long_age: int,high_speed: int, sum_teeth: int):
#         super().__init__(animal_type,color,long_age)
#         self.high_speed=high_speed
#         self.sum_teeth=sum_teeth
    

# class Cat(Animal):
#     def __init__(self,animal_type: str, color: str, long_age: int,high_speed: int, sum_teeth: int):
#         super().__init__(animal_type,color,long_age)
#         self.high_speed=high_speed
#         self.sum_teeth=sum_teeth
# class Horse(Animal):
#     def __init__(self,animal_type: str, color: str, long_age: int,high_speed: int, sum_teeth: int):
#         super().__init__(animal_type,color,long_age)
#         self.high_speed=high_speed
#         self.sum_teeth=sum_teeth
   
    
    
# dog=Dog("it","malla",5,40,12)
# cat=Cat("mushuk","sariq",2,20,17)
# horse=Horse("ot","qora",12,70,15)

# lst=[dog,cat,horse]
# print("\n ekranga eng tez yugauradigan hayvon chiqarildi: ")
# max_speed=max(lst, key=lambda x:x.high_speed)
# print(max_speed.info())

# print("ekranga eng kop tishli hayvon chiqarildi: ")
# max_teeth=max(lst, key=lambda x:x.sum_teeth)
# print(max_teeth.info())


# problem 4
class Employee:
    def __init__(self,name: str, id: int, salary: int):
        self.name=name
        self.id=id
        self.salary=salary
    def display_info(self):
        return f"""
name: {self.name}
id:  {self.id}
salary: {self.salary}    
    """
class  Ishchi(Employee):
    def __init__(self,name: str,id: int,hourly_rate: int, hours_worked: int):
        super().__init__(name,id,None)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        self.salary=(self.hourly_rate*self.hours_worked)*30

        
class Raxbar(Employee):
    def __init__(self,name: str,id: int,hourly_rate, hours_worked):
        super().__init__(name,id,None)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        self.salary=(self.hourly_rate*self.hours_worked)*30
        
class Boshqaruvchi(Employee):
    def __init__(self,name: str,id: int,hourly_rate, hours_worked):
        super().__init__(name,id,None)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        self.salary=(self.hourly_rate*self.hours_worked)*30

ishchi=Ishchi("eldor",25364,10,8)
ishchi.calculate_salary()
print()
print("\tISHCHI")
print(ishchi.display_info())

raxbar=Raxbar("asror",19374,15,8)
raxbar.calculate_salary()
print("\tRAXBAR")
print(raxbar.display_info())

boshqaruvchi=Boshqaruvchi("shavkat",23789,20,7)
boshqaruvchi.calculate_salary()
print("\tBOSHQARUVCHI")
print(boshqaruvchi.display_info())




#  problem 5
# class Vehicle:
#     def __init__(self,type: str,model: str):
#         self.type=type
#         self.model=model
# class Car(Vehicle):
#     def __init__(self,type: str,model: str,num_doors: int,num_wheels: int):
#         super().__init__(type,model)
#         self.num_doors=num_doors
#         self.num_wheels=num_wheels
#     def info(self):
#         return f"""
#     **CAR**
# type: {self.type}
# model: {self.model}
# num_doors: {self.num_doors} ta
# num_wheels: {self.num_wheels} ta
#     """
# class Motorcycle(Vehicle):
#     def __init__(self,type: str,model: str,num_doors: int,num_wheels: int):
#         super().__init__(type,model)
#         self.num_doors=num_doors
#         self.num_wheels=num_wheels
#     def info(self):
#       return f"""
#   **MOTORCYCLE**
# type: {self.type}
# model: {self.model}
# num_doors: {self.num_doors} ta
# num_wheels: {self.num_wheels} ta
#     """
# class Helicopter(Vehicle):
#     def __init__(self,type: str,model: str,num_doors: int,num_wheels: int):
#         super().__init__(type,model)
#         self.num_doors=num_doors
#         self.num_wheels=num_wheels
#     def info(self):
#       return f"""
#   **HELICOPTER**
# type: {self.type}
# model: {self.model}
# num_doors: {self.num_doors} ta
# num_wheels: {self.num_wheels} ta
#     """
# class Plan(Vehicle):
#     def __init__(self,type: str,model: str,num_doors: int,num_wheels: int):
#         super().__init__(type,model)
#         self.num_doors=num_doors
#         self.num_wheels=num_wheels
#     def info(self):
#       return f"""
#   **PLAN**
# type: {self.type}
# model: {self.model}
# num_doors: {self.num_doors} 
# num_wheels: {self.num_wheels} ta
#     """

# car=Car("yengil mashena","BMW M5 CS",4,4)
# print(car.info())

# mototskyle=Motorcycle("motatsekl","skuter",None,2)
# print(mototskyle.info())

# helicopter=Helicopter("vertalyot","AS563mbe",2,3)
# print(helicopter.info())

# plan=Plan("samalyot","SU-35",1,3)
# print(plan.info())