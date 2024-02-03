class Texnika:
    def __init__(self,brand: str,model: str,type: str):
        self.brand=brand
        self.model=model
        self.type=type
    def info(self):
        return f"""
brand: {self.brand}
model: {self.model}
type:  {self.type}
    """
class Notebook(Texnika):
    def __init__(self,brand: str,model: str,type: str,vedio_card: int,ram: int,display: int):
        super().__init__(brand,model,type)
        self.vedio_card=vedio_card
        self.ram=ram
        self.display=display
    def more_info(self):
        return f"""
brand: {self.brand}
model: {self.model}
type:  {self.type}
vedio_card: {self.vedio_card}
ram: {self.ram}
display: {self.display}
"""


class Telivisions(Texnika):
    def __init__(self,brand: str,model: str,type: str,size: str,display: int):
        super().__init__(brand,model,type)
        self.size=size
        self.display=display
    def more_info(self):
        return f"""
brand: {self.brand}
model: {self.model}
type:  {self.type}
size: {self.size}
display: {self.display}

"""

class Smartphones(Texnika):
    def __init__(self,brand: str,model: str,type: str,sim_count: int):
         super().__init__(brand,model,type)
         self.sim_count=sim_count
    def more_info(self):
        return f"""
brand: {self.brand}
model: {self.model}
type:  {self.type}
sim_count:  {self.sim_count}

"""
    
    
texnika=Notebook("Iphone","15 pro max","qol telefon",512,16,100)
print(texnika.info())
print(texnika.more_info())
texnika1=Telivisions("Iphone","15 pro max","qol telefon","20 sm",100)
print(texnika1.more_info())
texnika2=Smartphones("Iphone","15 pro max","qol telefon",2)
print(texnika2.more_info())


        