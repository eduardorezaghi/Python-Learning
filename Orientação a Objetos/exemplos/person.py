class Person():
    eyes = 2
    legs = 2
    arms = 2
    torso = 1
    mouth = 1
    nose = 1

    def __init__(self, name, age, skin_color, eye_color, favorite_food):
        self.name = name
        self.age = age
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.favorite_food = favorite_food
    
    def _eat_favorite_food(self):
        """Privative method used when a person is eating his favorite food."""
        return f"{self.name} is eating his {self.favorite_food}."
    
    def eat(self,food):
        if food == self.favorite_food:
            print(f"{self._eat_favorite_food()}")