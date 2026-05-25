import pandas as pd


class CafeReports:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    # groupby(city)
    def group_by_city(self):
        grouped = self.df.groupby("city")["avg_check"].mean()

        print("Average Check by City:\n")
        print(grouped)

    # топ по рейтингу
    def top_by_rating(self):
        top_rating = self.df.sort_values(by="rating", ascending=False)

        print("\nTop Cafes by Rating:\n")
        print(top_rating)

    # топ по чеку
    def top_by_check(self):
        top_check = self.df.sort_values(by="avg_check", ascending=False)

        print("\nTop Cafes by Average Check:\n")
        print(top_check)