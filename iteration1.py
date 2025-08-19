# Iteration 2: Add Humidity, Wind Speed, and Validation

def temperature_model(x):
    a, b, c = 1, -5, 6
    return a*x*x + b*x + c

def humidity_model(x):
    p, q, r = 0.5, -3, 10
    return p*x*x + q*x + r

def wind_speed_model(x):
    m, n, k = 0.2, 1, 5
    return m*x*x + n*x + k

def validate(value):
    # Ensures weather values don’t go below zero
    return max(0, value)

def main():
    x = 2  # example input (e.g., time)
    
    temp = validate(temperature_model(x))
    hum = validate(humidity_model(x))
    wind = validate(wind_speed_model(x))
    
    print(f"Weather Prediction at x={x}:")
    print(f"  Temperature: {temp}")
    print(f"  Humidity: {hum}")
    print(f"  Wind Speed: {wind}")

if __name__ == "__main__":
    main()
