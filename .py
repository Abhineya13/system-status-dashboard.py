class WeatherReport:
    # Constructor
    def __init__(self, city, temperature, humidity, condition):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.condition = condition

    # Display method
    def display_report(self):
        print("=================================")
        print("          Weather Report")
        print("=================================")
        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature}°C")
        print(f"Humidity: {self.humidity}%")
        print(f"Condition: {self.condition}")
        print("=================================")

# Main block to run the program
if __name__ == "__main__":
    today = WeatherReport("New York", 22.5, 65, "Partly Cloudy")
    today.display_report()
