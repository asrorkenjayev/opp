class Circle:
    def __init__(self,radius: int,color: str):
        
        self.radius=radius
        self.color=color
    def get_radues(self):
        return self.radius
    def set_radues(self,new_radues: int):
        self.radius=new_radues
    def get_color(self):
        return self.color
    def set_color(self,new_color: str):
        self.color=new_color
st=Circle(15,"qora")
print(st.get_radues())
st.set_radues(28)
print(st.radius)
print(st.get_color())
st.set_color('qizil')
print(st.color)



