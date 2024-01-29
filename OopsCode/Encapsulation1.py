class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_gender(self,gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")

athlete = Athlete("Pranav","boy")

athlete.set_name("Maria")
athlete.set_gender("girl")
print("Athlete Name:",athlete.get_name(),"and her gender is",athlete.get_gender(),"and She is running:",end=" ")
athlete.running()

