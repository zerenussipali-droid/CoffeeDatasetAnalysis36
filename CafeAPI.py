import pandas as pd
import matplotlib.pyplot as plt
from fastapi import FastAPI
from fastapi.responses import FileResponse


class CafeAPI:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    # API подборки
    def top_cafes(self):
        top = self.df[self.df["rating"] >= 4.7]

        return top.to_dict(orient="records")

    # Scatter chart
    def create_scatter_chart(self):
        plt.scatter(self.df["avg_check"], self.df["rating"])

        plt.xlabel("Average Check")
        plt.ylabel("Rating")
        plt.title("Check vs Rating")

        plt.savefig("scatter.png")


analytics = CafeAPI("cafes.csv")

app = FastAPI()


@app.get("/top-cafes")
def get_top_cafes():
    return analytics.top_cafes()


@app.get("/scatter-chart")
def scatter_chart():
    analytics.create_scatter_chart()

    return FileResponse("scatter.png")