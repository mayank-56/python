class Temperature:
    def __init__(self, temp, scale):
        self.temp = temp
        self.scale = scale.lower()  # 'c' for Celsius, 'f' for Fahrenheit
    
    # Convert to Fahrenheit
    def convertFarenheit(self):
        if self.scale == 'c':
            f = (self.temp * 9/5) + 32
            print(f"{self.temp}°C = {f}°F")
        else:
            print(f"Temperature is already in Fahrenheit: {self.temp}°F")
    
    # Convert to Celsius
    def convertCelsius(self):
        if self.scale == 'f':
            c = (self.temp - 32) * 5/9
            print(f"{self.temp}°F = {c}°C")
        else:
            print(f"Temperature is already in Celsius: {self.temp}°C")


t1 = Temperature(25, 'C')
t1.convertFarenheit()  
t1.convertCelsius()    

t2 = Temperature(77, 'F')
t2.convertCelsius()    
t2.convertFarenheit()  
