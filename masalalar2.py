class Transport:
    def __init__(self,brand: str,model: str,color: str):
      
        self.__brand=brand
        self.__model=model
        self.__color=color
        
    def setBrand(self,newbrand: str):
        self.__brand=newbrand
    def setModel(self,newmodel: str):
        self.__model=newmodel
    def setColor(self,newcolor: str):
        self.__color=newcolor
        
    
        
    def get_info(self):
        return f"""
brand: {self.__brand}
model: {self.__model}
color: {self.__color}   
    """
    

class Car(Transport):
    def __init__(self,brand: str,model: str,color: str,speed: int,seatCount: int,manafucturedata: str):
    super().__init(setBrand,setModel,setColor)
    self.__speed=speed
    self.__seatCount=seatCount
    self.__manafucturedata=manafucturedata
    
    def set_speed(self,newspeed):
        self.__speed=newspeed
    def set_seatcount(self,new_seatcount):
        self.__seatcount=new_seatcount
    def set_manafucturedata(self,newdata):
        self.__manafucturedata=newdata
    
    def get_info(self):
        return f"""
brand: {self.__brand}
model: {self.__model}
color: {self.__color}
speed: {self.__speed}
seatCount: {self.__seatCount}
manafucturedata: {self.__manafucturedata}
    """
    

# class Truck(Transport):
#     def __init__(self,model: str,brand: str,color: str,weightcapacity):
#         super().__init__(brand,model,color)
#         self.___weightcapacity=weightcapacity
#     def get_info(self):
#         return f"""
# brand: {self.__brand}
# model: {self.__model}
# color: {self.__color}
# weightcapacity: {self.__weightcapacity}
# """

transport=Transport("BMW","M5 90s","qora")
print(transport.get_info())
transport.setBrand("Mersedes Benz")
transport.setModel("Sl_class")
transport.setColor("mocrey")
print(transport.get_info())


car=Car("chevrolet","nexia","oq",200,5,"12.03.2000")
print(transport.get_info())
car.set_speed(220)
car.set_seatcount(7)
car.set_manafucturedata("02.09.2006")
print(car.get_info())