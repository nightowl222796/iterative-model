cache = {} 
 
def temperature_model(x): return 1*x*x - 5*x + 6 
def humidity_model(x): return 0.5*x*x - 3*x + 10 
def wind_speed_model(x): return 0.2*x*x + 1*x + 5 
def validate(v): return max(0, v) 
 
def predict_all(x): 
    if x in cache: 
        print("Using cached result...") 
        return cache[x] 
    result = ( 
        validate(temperature_model(x)), 
        validate(humidity_model(x)), 
        validate(wind_speed_model(x)) 
    ) 
    cache[x] = result 
    return result 
 
def main(): 
    while True: 
        try: 
            x = float(input("Enter time (x): ")) 
        except ValueError: 
            print("Invalid input.") 
            continue 
 
        temp, hum, wind = predict_all(x) 
        print(f"Temperature: {temp}°C\nHumidity: {hum}%\nWind Speed: {wind} km/h") 
 
        if input("Predict again? (y/n): ").lower() != 'y': 
            break 
 
if __name__ == "__main__": 
    main()