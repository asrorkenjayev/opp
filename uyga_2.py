# class Rectangle:
#     def __init__(self,height: int,wedth: int):
#         self.height=height
#         self.wedth=wedth
#     def get_height(self):
#         return self.height
#     def set_height(self,new_height: int):
#         self.height=new_height
#     def get_wedth(self):
#         return self.wedth
#     def set_wedth(self,new_wedth: int):
#         self.wedth = new_wedth
#     def get_area(self):
#         return self.height*self.wedth
#     def get_peremetr(self):
#         return 2*(self.height+self.wedth)
#     def info(self):
#         return f"""
# boyi: {self.height} 
# eni:{self.wedth}
# yuzi:{self.get_area}
# peremetri:{self.get_peremetr}"""
    
# st=Rectangle(12,45)
# print("boyi ",st.get_height())
# st.set_height(34)
# print("ozgargan boyi ",st.height)
# print("eni ",st.get_wedth())
# st.set_wedth(21)
# print("ozgargan eni ",st.wedth)
# print("yuzi ",st.get_area())
# print("peremetri ",st.get_peremetr())

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst = nums
        count = math.factorial(len(lst))

        i = 1
        natija = [ lst ]

        while i < count:
            copy = lst.copy()
            random.shuffle(copy)
            if copy not in natija:
                natija.append(copy)
                i += 1
        return natija


