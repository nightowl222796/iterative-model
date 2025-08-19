def temperature_model(x):
    # Example: a quadratic model for temperature
    return -0.3 * x * x + 4 * x + 20  

def humidity_model(x):
    return 0.5 * x * x - 3 * x + 10

def wind_speed_model(x):
    return 0.2 * x * x + 1 * x + 5

def validate(value):
    return max(0, value)

def main():
    while True:
        try:
            x = float(input("Enter time (x): "))
        except ValueError:
            print("Invalid input.")
            continue

        print("Temperature:", validate(temperature_model(x)))
        print("Humidity:", validate(humidity_model(x)))
        print("Wind Speed:", validate(wind_speed_model(x)))

        again = input("Predict again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
