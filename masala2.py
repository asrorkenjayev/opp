class Employee:
  def __init__(self,surname: str,position: str,salary: int):
      self.surname=surname
      self.position=position
      self.salary=salary
class Enterprise_employee(Employee):
    def __init__(self,surname: str,position: str,salary: int,rating: int):
        super().__init__(surname,position,salary)
        self.rating=rating
      
    def update(self):
        if self.rating >= 60 and self.rating < 75:
            self.salary += self.salary * 0.2
        elif self.rating >= 75 and self.rating < 90:
            self.salary += self.salary * 0.4
        elif self.rating >=90 and self.rating<=100:
            self.salary += self.salary * 0.6
    
    def more_info(self):
        return f"""
surname: {self.surname}
position: {self.position}
salary:   {self.salary   }
rating:   {self.rating}
  """



e1 = Enterprise_employee("Toshmatov", "engineer", 2000000, 90)
e1.update()
print(e1.more_info())