#애니멀 클래스 만들기

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return (f"{self.age}살 먹은 짐승 {self.name}의 소리는 {self.voice}")
    

class Dog(Animal):
    def __init__(self, name, age):
        self.voice = "멍멍!!"
        super().__init__(name, age)
    
    def speak(self):
        return super().speak()


class Cat(Animal):
    def __init__(self, name, age):
        self.voice = "야옹야옹~~"
        super().__init__(name, age)
    
    def speak(self):
        return super().speak()
    


dog1 = Dog("바둑이", 3)
cat1 = Cat("나비", 5)

print(dog1.speak())
print(cat1.speak())