from abc import ABC, abstractmethod

class Animal(ABC):
   
    @abstractmethod
    def eat(self):
        pass
   
    @abstractmethod
    def move(self):
        pass

class Fish(Animal):
   
    def eat(self):
        return "Рыба ест водоросли."
   
    def move(self):
        return "Рыба плавает, двигая плавниками."

class Bird(Animal):
   
    def eat(self):
        return "Птица ест семена, насекомых."
   
    def move(self):
        return "Птица летает, махая крыльями."

nemo = Fish()
print(nemo.eat())
print(nemo.move())
eagle = Bird()
print(eagle.eat())
print(eagle.move())