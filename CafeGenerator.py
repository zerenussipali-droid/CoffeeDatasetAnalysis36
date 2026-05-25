import pandas as pd
import json


class CafeGenerator:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def cafes_by_city(self, city):
        cafes = self.df[self.df["city"] == city]

        return cafes.to_dict(orient="records")

    def save_to_json(self, city):
        cafes = self.cafes_by_city(city)

        filename = f"{city}_cafes.json"

        with open(filename, "w") as file:
            json.dump(cafes, file, indent=4)

        print(f"{filename} created successfully!")