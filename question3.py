#도형 클래스 만들기

class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        answer = (self.radius**2)*3.14
        return (f"당신이 고른 원의 반지름이 {self.radius}cm 라면, 그 원의 넓이는 {answer}cm² 입니다.")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        answer = (self.width*self.length)
        return (f"당신이 고른 사각형의 가로변이 {self.width}cm 이고, 세로변이 {self.length}cm 라면, 그 사각형의 넓이는 {answer}cm² 입니다.")


cir1 = Circle(5)
Rec1 = Rectangle(3,5)

print(cir1.get_area())
print(Rec1.get_area())