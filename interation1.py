# Basic quadratic model for temperature prediction 
def temperature_model(x): 
a, b, c = 1, -5, 6 
return a*x*x + b*x + c 
def main(): 
x = 2  # example input (e.g., time) 
temp = temperature_model(x) 
print(f"Predicted temperature at x={x} is {temp}") 
if __name__ == "__main__": 
main() 
Iteration 2: Add Humidity, Wind Speed, Validation 