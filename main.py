
from CafeAnalytics import CafeAnalytics
from CafeGenerator import CafeGenerator
from CafeReports import CafeReports


print("===== CafeAnalytics =====")

board = CafeAnalytics("cafes.csv")

board.top_rated_cafe()
board.cheapest_cafe()
board.cafes_by_city("Almaty")


print("\n===== CAFE GENERATOR =====")

generator = CafeGenerator("cafes.csv")

city = input("Enter city: ")

generator.save_to_json(city)


print("\n===== CAFE REPORTS =====")

analytics = CafeReports("cafes.csv")

analytics.group_by_city()
analytics.top_by_rating()
analytics.top_by_check()


print("\n===== FASTAPI =====")
print("Run this command in terminal:")
print("python -m uvicorn CafeAPI:app --reload")