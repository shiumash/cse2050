# main.py
from weather_analysis import *

def weather_analyze(file_path):
    """
    returns a python dictionary off the statistics from weather data when given the file path
    """
    data = {}
    weather_data = read_weather_data(file_path)
    data["average_temperature"] = calculate_average_temperature(weather_data)
    data["total_rainfall"] = calculate_total_rainfall(weather_data)
    data["highest_temperature"] = find_highest_temperature(weather_data)
    data["lowest_temperature"] = find_lowest_temperature(weather_data)
    data["most_rainfall"] = find_day_with_most_rainfall(weather_data)

    return data


if __name__ == "__main__":
    
    results = weather_analyze("weather_data.txt") #or the path to the file
    print(results)