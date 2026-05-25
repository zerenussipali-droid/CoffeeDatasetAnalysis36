import pandas as pd

class Cafe:
    def __init__(self, cafe, city, avg_check, rating):
        self.cafe = cafe
        self.city = city
        self.avg_check = avg_check
        self.rating = rating

    def to_dict(self):
        return {
            "cafe": self.cafe,
            "city": self.city,
            "avg_check": self.avg_check,
            "rating": self.rating
        }

cafes = [
    Cafe("Coffee Boom", "Almaty", 4500, 4.8),
    Cafe("Urban Coffee", "Astana", 5200, 4.6),
    Cafe("Qazaq Coffee", "Shymkent", 3900, 4.7),
    Cafe("Cappuccino", "Almaty", 6100, 4.9),
    Cafe("Coffee Point", "Karaganda", 3400, 4.5)
]

data = [cafe.to_dict() for cafe in cafes]
df = pd.DataFrame(data)
df.to_csv("cafes.csv", index=False)

print("cafes.csv file created")