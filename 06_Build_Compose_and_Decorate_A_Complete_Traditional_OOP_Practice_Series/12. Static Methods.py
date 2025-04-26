class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
print(TemperatureConverter.celsius_to_fahrenheit(0))    
print(TemperatureConverter.celsius_to_fahrenheit(100))  
print(TemperatureConverter.celsius_to_fahrenheit(37))  