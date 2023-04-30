#자동차 클래스 만들기

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed_now = 100

    def accelerate(self):
        self.speed_now += 20
    
    def brake(self):
        self.speed_now -= 20

    def get_speed(self):
        return (f"현재 당신 차의 차종은 {self.model}, 색깔은 {self.color} 이고, 속도는 {self.speed_now}입니다.")
    


car1 = Car("bentz", "black")
car1.accelerate()

print(car1.get_speed())