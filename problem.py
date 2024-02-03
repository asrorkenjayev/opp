# problem3
class Employee:
    def __init__(self,id: str,firstname: str,lastname: str,salary: int):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    def newid(self,newId: str):
        self.id = newId
    def getfirstname(self,newfirstname: str):
        self.firstname=newfirstname
        
    def info(self):
        return f"""
id:         {self.id}
firstname:  {self.firstname}
lastname:   {self.lastname}
salary:     {self.salary}
    """
        
    
st = Employee("19374","Asror","Kenjayev",10_000)
st1 = Employee("15940","Botir","Qodirov",9_000)
employer=[st,st1]
st.newid('2596')
st.getfirstname("Eldor")
for employe in employer:
    print(employe.info())



# problem2
# class Son:
#     a=int(input("a: "))
    
#     def toq_juft(self):
#         if self.a%2:
#             print("toq")
#         else:
#             print("juft")
# a = Son()
# a.toq_juft()


# problem1
# class Son:
#     num = int(input("num: "))
#     def plus_minus(self):
#         if self.num>0:
#             print("musbat")
#         else:
#             print("manfiy")

# s = Son()
# s.plus_minus()

