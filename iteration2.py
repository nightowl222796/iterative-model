# Predicts temperature, humidity, and wind speed 

def temperature_model(x):
    return 1 * x * x - 5 * x + 6

def humidity_model(x):
    return 0.5 * x * x - 3 * x + 10

def wind_speed_model(x):
    return 0.2 * x * x + 1 * x + 5

def validate(value):
    return max(0, value)

def main():
    x = 2
    print("Weather Prediction at x =", x)
    print("Temperature:", validate(temperature_model(x)))
    print("Humidity:", validate(humidity_model(x)))
    print("Wind Speed:", validate(wind_speed_model(x)))

if __name__ == "__main__":
    main()
