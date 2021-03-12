# class Tiger():
#     def __init__(self, age, color, weight, hp):
#         self.age = age
#         self.color = color
#         self.weight = weight
#         self.hp = hp
        
#     def __str__(self):
#         return f"This tiger is {self.age} years old, and weighs {self.weight} lbs."

#     def roar(self):
#         print("The tiger roars")
        
#     def damage(self, damagetaken=0):
#         self.hp -= damagetaken
#         print(f"This tiger took {damagetaken} and now has {self.hp} hp.")




# if __name__ == "__main__":
#     t1 = Tiger(age=42, color="white", weight=600, hp=100)
#     t1.roar()
#     t1.damage()
import time

class Movie():
    
    def __init__(self, name, rating, release_date, duration, countdown):
        self.name = name
        self.rating = rating
        self.release_date = release_date
        self.duration = duration
        self.countdown = countdown
        
    def __str__(self):
        return f"{self.name} has a rating of {self.rating}/10 and was released in {self.release_date}. It is {self.duration} minutes long."

    def play(self):
        for i in range(self.countdown, 0, -1):
            print(i)
            
        print("The movie has begun!")
        
        for i in range(0, self.duration, 1):
            print(i)
            time.sleep (1)
        # for(int i = 0; i < 10; i++) {
            
        # }
    
    
    
if __name__ == "__main__":
    movie1 = Movie(name="53rd jump street", rating=4.5, release_date=2021, duration=69, countdown=10)
    print(movie1)
    movie1.play()