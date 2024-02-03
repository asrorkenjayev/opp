# class Avto:
#     def __init__(self,model,rang,karobka ,narh,tezlik,kilometr=0):
#         self.model=model 
#         self.rang=rang   
#         self.karobka=karobka  
#         self.narh=narh 
#         self.tezlik=tezlik   
#         self.kilometr=kilometr

#     def malumotni_chiqar(self):
#         print(f"""
# model: {self.model}
# rang: {self.rang}
# karobka: {self.karobka}
# narh: {self.narh}
# tezlik:{self.tezlik}
# kilometr: {self.kilometr}
# """)        

# avto1 = Avto("Toyota supra", "Oq", "Avtomatik",350000, 320)
# avto1.malumotni_chiqar()

# class Avtasalon:
#     def __init__(self,salon_nomi: str,manzil: str,sotuvdagi_avtamabillar):
#         self.salon_nomi=salon_nomi
#         self.manzil=manzil
#         self.sotuvdagi_avtamabillar=sotuvdagi_avtamabillar
        
        
#     def __str__(self):
#         return f"""
# salon_nomi: {self.salon_nomi}
# manzil: {self.manzil}
# salondagi_avtamabillar: {self.sotuvdagi_avtamabillar}
    
#     """
# salon=Avtasalon("GM","asaka","damas,matiz,cobalt,jentra")
# print(salon)

# class Avto:
#     def __init__(self,model,rang,karobka ,narh,tezlik,kilometr=0):
#         self.model=model 
#         self.rang=rang   
#         self.karobka=karobka  
#         self.narh=narh 
#         self.tezlik=tezlik   
#         self.kilometr=kilometr

#     def malumotni_chiqar(self):
#         return f"""
# model:    {self.model}    
# rang:     {self.rang}
# karobka:  {self.karobka}
# narh:     {self.narh}
# tezlik:   {self.tezlik}
# kilometr: {self.kilometr}
# """
#     def update_km(self, yangi_km):
#         self.kilometr = yangi_km

# avto1 = Avto("Toyota supra", "Oq", "Avtomatik",200000, 350)
# print(avto1.malumotni_chiqar())

# avto1.update_km(300)
# print(avto1.malumotni_chiqar())

# class Avtosalon:
#     def __init__(self, salon_nomi, manzili, avtomobillar=None):
#         self.salon_nomi = salon_nomi
#         self.manzili = manzili
#         if avtomobillar is None:
#             self.avtomobillar = []
#         else:
#             self.avtomobillar = avtomobillar

#     def avtomobil_qoshish(self, avto):
#         self.avtomobillar.append(avto)

#     def avtomobillarni_chiqarish(self):
#         for avto in self.avtomobillar:
#             print(avto.malumotni_chiqar())
# salon1 = Avtosalon("Maxsus Avtosalon", "Toshkent shahri, Oybek tumani, Alisher Navoi ko'chasi, 12-uy")
# avto1 = Avto("Toyota supra", "Oq", "Avtomatik", 350000, 350)
# avto2 = Avto("Chevrolet Malibu", "Qora", "Avto", 250000, 210)
# salon1.avtomobil_qoshish(avto1)
# salon1.avtomobil_qoshish(avto2)
# salon1.avtomobillarni_chiqarish()

# class Transport:
#     def __init__(self,brand: str,model: str,type: str):
#         self.brand=brand
#         self.model=model
#         self.type=type
        
#     def info(self):
#         return f"""
# brand: {self.brand}
# model: {self.model}
# type:  {self.type}
#     """
    
# class Elantrocars(Transport):
#     def __init__(self,brand: str,model: str,type: str,batary_life : int,charging_time: str):
#         super().__init__(model,brand,type)
#         self.batary_life=batary_life
#         self.charging_time=charging_time
#     def more_info(self):
#         return f"""
#     "" Elantrocar""
# brand: {self.brand}
# model: {self.model}
# type:  {self.type}
# batary_life: {self.batary_life}soat
# charging_time: {self.charging_time}minut

#     """
        


# class Sportcars(Transport):
#     def __init__(self,brand: str,model: str,type,motor: str,color: str):
#         super().__init__(model,brand,type)
#         self.motor=motor
#         self.color=color
#     def more_info(self):
#        return f"""
#    ""Sportcar""
# brand: {self.brand}
# model: {self.model}
# type:  {self.type}
# motor: {self.motor}
# color: {self.color}
#     """
# class Truck(Transport):
#     def __init__(self,brand: str,model: str,type: str,motor: str,height: int,long: int,weight: int):
#          super().__init__(model,brand,type)
#          self.motor=motor
#          self.height=height
#          self.long=long
#          self.weight=weight
    
#     def more_info(self):
#        return f"""
#    ""TRUCK""
# brand: {self.brand}
# model: {self.model}
# type:  {self.type}
# motor: {self.motor}
# height: {self.height}metr
# long:  {self.long}metr
# weight: {self.weight}tonna
#     """
        
# elantro=Elantrocars("huyundai","sanata","yengil mashena",8,30)
# print(elantro.more_info())

# sport_car=Sportcars("bugatti","chiron","sport mashena","V12","qora")
# print(sport_car.more_info())

# truck=Truck("Msedes_benz","eActros 600","yuk mashena","12 L",3,32,50)
# print(truck.more_info())

# class University:
#     def __init__(self,university):
#         self.university=university
#     def info(self):
#         return f"""
#     ***UNIVERSITY***
# university:  {self.university}
#     """
# class Staf(University):
#     def __init__(self,university,first_name: str,last_name: str,age: int):
#         super().__init__(university)
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#     def staf_info(self):
#         return f"""
#     ***STAFF***
# university: {self.university}
# first_name: {self.first_name}
# last_name:  {self.last_name}   
# age: {self.age} 
#     """

# class Student(Staf):
#     def __init__(self,university,first_name: str,last_name: str,age: int,group: str):
#         super().__init__(university,first_name,last_name,age)
#         self.group=group
#     def more_info(self):
#         return f"""
#     ***STUDENT***
# university: {self.university}
# first_name: {self.first_name}
# last_name:  {self.last_name}   
# age: {self.age} 
# group: {self.group}
#     """
    
# class Teacher(Staf):
    
#     def __init__(self,university,first_name: str,last_name: str,age: int,position: str,subject: str):
#         super().__init__(university,first_name,last_name,age)
#         self.position=position
#         self.subject=subject
    
#     def more_info(self):
#         return f"""
#     ***TEACHER***
# university: {self.university}
# first_name: {self.first_name}
# last_name:  {self.last_name}   
# age: {self.age}
# position: {self.position}
# subject:  {self.subject} 
#     """
    
# class Otherstaff(Staf):
#     def __init__(self,university,first_name: str,last_name: str,age: int,position: str):
#         super().__init__(university,first_name,last_name,age)
#         self.position=position
        
    
#     def more_info(self):
#         return f"""
#     ***OTHERSATAFF***
# university: {self.university}
# first_name: {self.first_name}
# last_name:  {self.last_name}   
# age: {self.age}
# position: {self.position}
# """

# university=University("cambridge")
# print(university.info())

# staf=Staf("milliy","eldor","baxramov",21)
# print(staf.staf_info())

# student=Student("yuridik","nazar","yoqubov",19,'N65')
# print(student.more_info())

# teacher=Teacher("narxoz","numonjon","baxridinov",46,"diktor","None")
# print(teacher.more_info())

# other=Otherstaff("Moliya","eldor","mirzaqulov",23,"boshliq")
# print(other.more_info())

