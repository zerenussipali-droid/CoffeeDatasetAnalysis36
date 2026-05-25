import pandas as pd


class CafeAnalytics:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def top_rated_cafe(self):
        top = self.df.loc[self.df["rating"].idxmax()]

        print("Top Rated Cafe:\n")
        print(top)


    def cheapest_cafe(self):
        cheap = self.df.loc[self.df["avg_check"].idxmin()]

        print("\nCheapest Cafe:\n")
        print(cheap)


    def cafes_by_city(self, city):
        cafes = self.df[self.df["city"] == city]

        print(f"\nCafes in {city}:\n")
        print(cafes)