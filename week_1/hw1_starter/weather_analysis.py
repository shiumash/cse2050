# Instructions:
# 1. **Remove the TODO comment and pass statement** once you’ve completed the function implementation.
#    - The TODO and pass are placeholders indicating that the function is not yet complete.
#    - Once the function is implemented, these should be removed to keep the code clean.
# 
# 2. **Best Coding Practices**:
#    - In professional programming, finalizing the code means removing unnecessary placeholders.
#    - This ensures your code is ready for review, testing, and does not contain clutter.
# 
# 3. **Adding Docstrings**:
#    - After removing TODO and pass, add a **docstring** for each function.
#    - The docstring should explain the function’s purpose, parameters, and expected output.
#    - Proper documentation improves code readability and helps with debugging and maintenance.


def read_weather_data(file_path: str) -> list[tuple[str, float, float]]:
    """
    Reads weather data from a file. Function takes file path and returns a list of tuples for the weather data
    """
    result = []
    with open(file_path, "r") as f:
        for row in f.readlines():
            row = row.strip().split(",")
            result.append((row[0], float(row[1]), float(row[2])))
    
    return result

def calculate_average_temperature(weather_data: list[tuple[str, float, float]]) -> float:
    """
    takes the weather data and returns the average temperature
    """
    average_temp = sum(data[1] for data in weather_data) / len(weather_data)
    
    return average_temp
    
    

def calculate_total_rainfall(weather_data: list[tuple[str, float, float]]) -> float:
    """
    TODO: Takes in the weather data and returns the total rainfall.
    """
    total_rainfall = 0
    for data in weather_data:
        total_rainfall += data[2]
    
    return total_rainfall

def find_highest_temperature(weather_data: list[tuple[str, float, float]]) -> float:
    """
    Takes in weather data and returns a tuple of the day with the highest temperature and temperature
    """
    highest_temp = max(data[1] for data in weather_data)
    for data in weather_data:
        if data[1] == highest_temp:
            highest_day = data[0]

    return highest_day, highest_temp


def find_lowest_temperature(weather_data: list[tuple[str, float, float]]) -> float:
    """
    Takes in weather data and returns a tuple of the lowest day and lowest temperature
    """
    lowest_temp = min(data[1] for data in weather_data)
    for data in weather_data:
        if data[1] == lowest_temp:
            lowest_day = data[0]

    
    return lowest_day, lowest_temp

def find_day_with_most_rainfall(weather_data: list[tuple[str, float, float]]) -> str:
    """
    TODO: Takes in weather data and returns a tuple of the day with the most rainfall and the amount of rainfall
    """
    highest_rainfall_day = ""

    most_rainfall = max(data[2] for data in weather_data)
    for data in weather_data:
        if data[2] == most_rainfall:
            highest_rainfall_day = data[0]

    return highest_rainfall_day, most_rainfall

'''
data = read_weather_data('weather_data.txt')
print(find_lowest_temperature(data))
print(find_day_with_most_rainfall(data))
print(find_highest_temperature(data))
print(calculate_average_temperature(data))
print(calculate_total_rainfall(data))
'''