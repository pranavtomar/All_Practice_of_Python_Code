class Classroom:
    classroom_list = 0
    @classmethod
    def search_classroom(cls, class_room):
        Classroom.classroom_list = class_room
        if Classroom.classroom_list.lower() == "found":
            return "Found"
        else:
            return -1
print(Classroom.search_classroom("FOund"))